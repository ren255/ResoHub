import scrapy
from scrapy import signals
from scrapy.http.response import Response

from scraper.items import SubjectCatalogItem
from ..services import url_generator, PageType, TextFile, ItemCollection

import json
import pandas as pd
from time import time
from io import StringIO


class SubjectCatalogSpider(scrapy.Spider):
    name = "subject_catalog"
    allowed_domains = ["syllabus.kosen-k.go.jp"]

    def __init__(self, uuid, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = uuid
        self.start_time = time()

    async def start(self):
        subjects_file = TextFile(self.scrape_id, "subject_id", "jsonl")
        subjects = await subjects_file.read_as_lines()
        departments_file = TextFile(self.scrape_id, "department_id", "jsonl")
        departments = await departments_file.read_as_lines()

        # if subjects:
        #     departments = await self.resume(subjects, subjects_file, departments)
        # else:
        #     print("no previous run")

        await subjects_file.write_file("")

        for department in departments:
            dept = json.loads(department)
            self.url = url_generator(
                PageType.SUBJECTS,
                school_id=dept["school_id"],
                department_id=dept["department_id"],
                year=2025,
            )
            yield scrapy.Request(self.url, callback=self.parse)

    async def resume(self, subjects, subjects_file, departments):
        last_subject = json.loads(subjects[-1])
        print(json.dumps(last_subject, ensure_ascii=False))

        # さいごの学科の入力直前まで戻す
        for i, subj_line in enumerate(subjects):
            subj = json.loads(subj_line)
            if (
                subj["school_id"] == last_subject["school_id"]
                and subj["department_id"] == last_subject["department_id"]
            ):
                subjects = subjects[i:]
                await subjects_file.write_file("\n".join(subjects))
                break

        # 最後に処理された学科の位置を探す
        for i, dept_line in enumerate(departments):
            dept = json.loads(dept_line)
            print(f"{(i - 1 )=}")
            if (
                dept["school_id"] == last_subject["school_id"]
                and dept["department_id"] == last_subject["department_id"]
            ):
                # 最後一つ手前から再開
                remaining = departments[i - 1 :]
                progress = len(remaining) / len(departments)
                print(
                    f"found previous run: school_id={last_subject['school_id']}, "
                    f"department_id={last_subject['department_id']}"
                )
                print(
                    f"resuming: {len(remaining)} of {len(departments)} "
                    f"({progress:.2%} remaining)"
                )
                return remaining

        return departments

    def parse(self, response: Response):
        df = pd.read_html(StringIO(response.text), match="学年別週当授業時数")[0]
        skip_first_rows = 4
        column_names = [
            "subject_type",
            "subject_classification",
            "subject_name",
            "subject_code",
            "credit_type",
            "credits",
        ]
        df = df.iloc[skip_first_rows:]
        df.columns = column_names + df.columns.tolist()[len(column_names) :]

        for row in df.itertuples():
            # subject urlは無いことがあるため取得しない
            yield SubjectCatalogItem(
                url_source=self.url,
                scrape_id=self.scrape_id,
                name=row.subject_name,
                subject_code=row.subject_code,
            )

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(SubjectCatalogSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    async def spider_closed(self, spider):
        items = ItemCollection(self.scrape_id, SubjectCatalogItem.__name__)
        file = TextFile(self.scrape_id, "subject_id", "jsonl")
        jsons = await items.get_data()
        await file.write_file("\n".join(jsons))

        print(
            f"\nSubjectCatalogSpider:{self.scrape_id} done ------------\ntook: {time() - self.start_time:.2f}"
        )
