import scrapy


class DepartmentsOverviewSpider(scrapy.Spider):
    name = "departments_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    start_urls = ["https://syllabus.kosen-k.go.jp"]

    def parse(self, response):
        pass
