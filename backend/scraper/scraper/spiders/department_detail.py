import scrapy
from scrapy import signals
from scrapy.http.response import Response

from scraper.items import DepartmentDetailItem
from ..services import url_generator, PageType, TextFile, ItemCollection

import json
import pandas as pd
from time import time
from io import StringIO
import datetime


class DepartmentDetailSpider(scrapy.Spider):
    """
    -> department overview
    各学科の有効な入学年度を特定
    -> subject catalog
    """

    name = "subject_catalog"
    allowed_domains = ["syllabus.kosen-k.go.jp"]

    def __init__(self, uuid, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = uuid
        self.start_time = time()

    async def start(self):
        departments_file = TextFile(self.scrape_id, "department_overview", "jsonl")
        departments = await departments_file.read_as_lines()

        for department in departments:
            dept = json.loads(department)
            url = url_generator(
                PageType.SUBJECTS,
                school_id=dept["school_id"],
                department_id=dept["department_id"],
                year=datetime.date.today().year,
            )
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response: Response):
        # 教科数を取得し存在する学科か確かめる
        df = pd.read_html(StringIO(response.text), match="学年別週当授業時数")[0]
        skip_first_rows = 4
        df = df.iloc[skip_first_rows:]
        subject_count = len(df)

        # 右上の開講年度ドロップダウンから取得
        urls = response.css(".dropdown-header a::attr(href)").getall()
        urls = urls[:-1]
        urls = [response.urljoin(url) for url in urls]

        # 存在しない学科の場合最古の開催年から取得し直す
        if not subject_count:
            yield scrapy.Request(response.urljoin(urls[-1]), callback=self.parse)

        # pipeline でurlの処理が行われる
        for url in urls:
            yield DepartmentDetailItem(
                scrape_id=self.scrape_id,
                url_source=url,
            )

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(DepartmentDetailSpider, cls).from_crawler(
            crawler, *args, **kwargs
        )
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    async def spider_closed(self, spider):
        items = ItemCollection(self.scrape_id, DepartmentDetailItem.__name__)
        file = TextFile(self.scrape_id, "department_id", "jsonl")
        jsons = await items.get_data()
        await file.write_file("\n".join(jsons))

        print(
            f"\n{DepartmentDetailSpider.__name__}: {self.scrape_id} done ------------\ntook: {time() - self.start_time:.2f}"
        )
