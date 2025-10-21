import scrapy
from scraper.items import CollegesOverviewItem
from ..services.url_manager import url_generator,PageType

class CollegesOverviewSpider(scrapy.Spider):
    name = "colleges_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    base_url = "https://syllabus.kosen-k.go.jp/"
    url = url_generator(PageType.SCHOOLS)

    def __init__(self, param1, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = param1
        
    def start_requests(self):
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
