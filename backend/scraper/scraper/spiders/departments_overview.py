import scrapy, json
from scrapy.http.response import Response
from core.models import ScrapyItem
from scraper.items import CollegesOverviewItem, DepartmentsOverviewItem


class DepartmentsOverviewSpider(scrapy.Spider):
    name = "departments_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]

    def __init__(self, param1, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = param1

    def start_requests(self):
        for item in ScrapyItem.objects.all():
            if (
                item.scrape_id != self.scrape_id
                or item.item_name != CollegesOverviewItem.__name__
            ):
                continue

            # dataフィールドからJSONをパースしてURLを取得
            item_data = json.loads(item.data)
            url_college = item_data.get("url_college")

            if url_college:
                yield scrapy.Request(url_college, callback=self.parse)

    def parse(self, response: Response):
        names = response.css(".list-group-item-heading::text").getall()
        links = response.css(".col-md-6+ .col-md-6")
