import scrapy
from scraper.items import CollegesOverviewItem


class CollegesOverviewSpider(scrapy.Spider):
    name = "colleges_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    start_urls = ["https://syllabus.kosen-k.go.jp"]

    def __init__(self, param1, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = param1

    def parse(self, response):
        schools = response.css(".btn-default")
        print(f"processing {len(schools)} schools")
        for school in schools:
            name = school.css("::text").get()
            if not "高等専門学校" in name:
                continue
            url = self.start_urls[0] + school.css("::attr(href)").get()

            yield CollegesOverviewItem(
                url_source="https://syllabus.kosen-k.go.jp/Pages/PublicSchools",
                scrape_id=self.scrape_id,
                name=name,
                url_college=url,
            )
