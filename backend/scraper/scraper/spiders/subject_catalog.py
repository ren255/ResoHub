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
        departments_file = TextFile(self.scrape_id, "department_id", "jsonl")
        departments = await departments_file.read_as_lines()
        await subjects_file.delete()

        for department in departments:
            dept = json.loads(department)
            url = url_generator(
                PageType.SUBJECTS,
                school_id=dept["school_id"],
                department_id=dept["department_id"],
                year=dept["admission_year"],
            )
            yield scrapy.Request(url, callback=self.parse)

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
        df["subject_name"] = df["subject_name"].str.split("  ").str[0]

        urls = response.css(".mcc-show::attr(href)").getall()
        urls = [response.urljoin(url) for url in urls]
        for row, url in zip(df.itertuples(), urls):
            # subject urlは無いことがあるため取得しない
            yield SubjectCatalogItem(
                scrape_id=self.scrape_id,
                name=row.subject_name,
                subject_code=row.subject_code,
                url_source=response.url,
                subject_url=url,
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
            f"\nSubjectCatalogSpider: {self.scrape_id} done ------------\ntook: {time() - self.start_time:.2f}"
        )
