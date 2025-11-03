import scrapy
from scrapy import signals
from scrapy.http.response import Response

from scraper.items import SubjectDetailItem, SubjectContentItem
from ..services import (
    url_generator,
    PageType,
    TextFile,
    ItemCollection,
    SpiderProcessLogger,
)

import json
import pandas as pd
from time import time
from io import StringIO


class SubjectDetailSpider(scrapy.Spider):
    name = "subject_detail"
    allowed_domains = ["syllabus.kosen-k.go.jp"]

    def __init__(self, uuid, school_id=None, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = uuid
        self.school_id = school_id
        self.process_logger = SpiderProcessLogger(self)

    async def start(self):
        self.process_logger.start()
        subjects_file = TextFile(self.scrape_id, "subject_id", "jsonl")
        subject_details_file = TextFile(self.scrape_id, "subject_detail", "jsonl")
        file = TextFile(self.scrape_id, "subject_contents", "jsonl")
        await file.delete()
        subjects = await subjects_file.read_as_lines()
        if self.school_id:
            subjects = [
                subject
                for subject in subjects
                if json.loads(subject)["school_id"] == self.school_id
            ]
        await subject_details_file.delete()

        for subject in subjects:
            sub = json.loads(subject)
            url = url_generator(
                PageType.SYLLABUS,
                school_id=sub["school_id"],
                department_id=sub["department_id"],
                subject_code=sub["subject_code"],
                year=sub["admission_year"],
            )
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response: Response):
        try:
            detail_df = pd.read_html(
                StringIO(response.text), match="単位の種別と単位数"
            )[0]
            credit_type, credits = detail_df.loc[3, 3].split(": ")
            yield SubjectDetailItem(
                scrape_id=self.scrape_id,
                subject_name=detail_df.loc[1, 1],
                subject_type=detail_df.loc[3, 1],
                subject_classification=detail_df.loc[2, 3],
                credit_type=credit_type,
                credits=credits,
                admission_year=detail_df.loc[0, 3],
                grade=detail_df.loc[4, 3],
                teachers=detail_df.loc[7, 1],
                textbooks=detail_df.loc[6, 1],
                week_hour=detail_df.loc[5, 3],
                open_period=detail_df.loc[0, 3],
                url_source=response.url,
            )
            self.process_logger.processed()

            quarters = response.css("th.bg-::text").getall()
            # quarters = [quarter.strip("Q") for quarter in quarters]
            weeks = response.css(".week_number::text").getall()
            weeks = [week.strip("週") for week in weeks]
            course_contents = response.css(".week_number+ td::text").getall()
            course_contents = [content.strip() for content in course_contents]
            goals = response.css("#lessonsTable td+ td::text").getall()
            goals = [goal.strip() for goal in goals]

            for quarter, week, content, goal in zip(
                quarters, weeks, course_contents, goals
            ):
                yield SubjectContentItem(
                    url_source=response.url,
                    scrape_id=self.scrape_id,
                    quarter=quarter,
                    week=week,
                    content=content,
                    goal=goal,
                )
                self.process_logger.processed()

            score_dest = pd.read_html(StringIO(response.text), match="総合評価割合")[0]
        except Exception as e:
            print(f"Error: '{e}' at : {response.url}")

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(SubjectDetailSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    async def spider_closed(self, spider):
        items = ItemCollection(self.scrape_id, SubjectDetailItem.__name__)
        file = TextFile(self.scrape_id, "subject_detail", "jsonl")
        jsons = await items.get_data()
        await file.write_file("\n".join(jsons))

        items = ItemCollection(self.scrape_id, SubjectContentItem.__name__)
        file = TextFile(self.scrape_id, "subject_contents", "jsonl")
        jsons = await items.get_data()
        await file.write_file("\n".join(jsons))

        self.process_logger.complete()
