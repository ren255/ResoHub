import scrapy


class CollegesOverviewSpider(scrapy.Spider):
    name = "colleges_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    start_urls = ["https://syllabus.kosen-k.go.jp"]

    def parse(self, response):
        pass
