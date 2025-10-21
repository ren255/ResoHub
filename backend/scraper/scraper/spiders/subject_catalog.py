import scrapy


class SubjectCatalogSpider(scrapy.Spider):
    name = "subject_catalog"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    start_urls = ["https://syllabus.kosen-k.go.jp"]

    def parse(self, response):
        pass
