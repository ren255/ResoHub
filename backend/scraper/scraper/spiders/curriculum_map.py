import scrapy


class CurriculumMapSpider(scrapy.Spider):
    name = "curriculum_map"
    allowed_domains = ["syllabus.kosen-k.go.jp"]
    start_urls = ["https://syllabus.kosen-k.go.jp"]

    def parse(self, response):
        pass
