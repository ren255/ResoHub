import scrapy, json
from scrapy import signals
from scrapy.http.response import Response

from scraper.items import DepartmentsOverviewItem
from ..services import url_generator, PageType, TextFile, ItemCollection
from time import time


class DepartmentsOverviewSpider(scrapy.Spider):
    name = "departments_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]

    def __init__(self, uuid, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = uuid
        self.start_time = time()

    async def start(self):
        file = TextFile(self.scrape_id, "school_id", "jsonl")
        schools = await file.read_as_lines()
        for school in schools:
            school = json.loads(school)
            url = url_generator(PageType.DEPARTMENTS, school_id=school["school_id"])
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response: Response):
        names = response.css(".list-group-item-heading::text").getall()
        links = response.css(".btn-sm:nth-child(1)::attr(href)").getall()
        for name, link in zip(names, links):
            yield DepartmentsOverviewItem(
                scrape_id=self.scrape_id,
                name=name,
                url_source=response.url,
                department_url=link,
            )

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(DepartmentsOverviewSpider, cls).from_crawler(
            crawler, *args, **kwargs
        )
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    async def spider_closed(self, spider):
        items = ItemCollection(self.scrape_id, DepartmentsOverviewItem.__name__)
        file = TextFile(self.scrape_id, "department_overview", "jsonl")
        jsons = await items.get_data()
        await file.write_file("\n".join(jsons))

        print(
            f"\nDepartmentsOverviewSpider: {self.scrape_id} done ------------\ntook: {time() - self.start_time:.2f}"
        )
