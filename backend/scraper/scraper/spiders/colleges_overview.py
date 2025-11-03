import scrapy
from scrapy import signals
from scraper.items import CollegesOverviewItem
from ..services import (
    url_generator,
    url_analyzer,
    PageType,
    ItemCollection,
    TextFile,
    SpiderProcessLogger,
)
from time import time


class CollegesOverviewSpider(scrapy.Spider):
    name = "colleges_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    base_url = "https://syllabus.kosen-k.go.jp/"
    url = url_generator(PageType.SCHOOLS)

    def __init__(self, uuid, school_id=None, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = uuid
        self.school_id = school_id
        self.process_logger = SpiderProcessLogger(self)

    async def start(self):
        self.process_logger.start()
        items = ItemCollection(self.scrape_id, CollegesOverviewItem.__name__)
        await items.delete_all()
        file = TextFile(self.scrape_id, "school_id", "jsonl")
        await file.delete()
        yield scrapy.Request(self.url, callback=self.parse)

    def parse(self, response):
        schools = response.css(".btn-default")
        print(f"processing {len(schools)} schools")
        for school in schools:
            name = school.css("::text").get()
            if not "高等専門学校" in name:
                continue
            url = response.urljoin(school.css("::attr(href)").get())

            if self.school_id and self.school_id != url_analyzer(url)["school_id"]:
                continue

            yield CollegesOverviewItem(
                scrape_id=self.scrape_id,
                name=name,
                url_source=response.url,
                url_college=url,
            )
            self.process_logger.processed()

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(CollegesOverviewSpider, cls).from_crawler(
            crawler, *args, **kwargs
        )
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    async def spider_closed(self, spider):
        items = ItemCollection(self.scrape_id, CollegesOverviewItem.__name__)
        file = TextFile(self.scrape_id, "school_id", "jsonl")
        jsons = await items.get_data()
        await file.write_file("\n".join(jsons))

        self.process_logger.complete()
