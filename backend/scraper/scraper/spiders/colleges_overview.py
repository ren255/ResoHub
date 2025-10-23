import scrapy
from scrapy import signals
from scraper.items import CollegesOverviewItem
from ..services import url_generator, PageType, ItemCollection, TextFile
from time import time


class CollegesOverviewSpider(scrapy.Spider):
    name = "colleges_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    base_url = "https://syllabus.kosen-k.go.jp/"
    url = url_generator(PageType.SCHOOLS)

    def __init__(self, uuid, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = uuid

    async def start(self):
        self.start_time = time()
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
            url = self.base_url + school.css("::attr(href)").get()

            yield CollegesOverviewItem(
                url_source=self.url,
                scrape_id=self.scrape_id,
                name=name,
                url_college=url,
            )

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
        await file.write_file("/n".join(jsons))

        print(
            f"CollegesOverviewSpider done ------------\ntook: {time() - self.start_time:.2f}"
        )
