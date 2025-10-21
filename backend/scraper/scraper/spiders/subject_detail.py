import scrapy


class SubjectDetailSpider(scrapy.Spider):
    name = "subject_detail"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    start_urls = ["https://syllabus.kosen-k.go.jp"]

    def parse(self, response):
        pass
