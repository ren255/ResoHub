import scrapy, json
from scrapy.http.response import Response
from core.models import ScrapyItem

from scraper.items import DepartmentsOverviewItem
from ..services.url_manager import url_analyzer, url_generator, PageType
from ..services.save_file import TextFile


class DepartmentsOverviewSpider(scrapy.Spider):
    name = "departments_overview"
    allowed_domains = ["syllabus.kosen-k.go.jp"]

    def __init__(self, param1, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = param1

    async def start(self):
        file = TextFile(self.scrape_id, "school_id", "jsonl")
        schools = await file.read_as_lines()
        for school in schools:
            school = json.loads(school)
            self.school_id = school["school_id"]
            self.url = url_generator(PageType.DEPARTMENTS, school_id=self.school_id)
            yield scrapy.Request(self.url, callback=self.parse)

    def parse(self, response: Response):
        names = response.css(".list-group-item-heading::text").getall()
        links = response.css(".btn-sm:nth-child(1)::attr(href)").getall()
        ids = [url_analyzer(link)["department_id"] for link in links]
        for name, id in zip(names, ids):
            yield DepartmentsOverviewItem(
                url_source=self.url,
                scrape_id=self.scrape_id,
                name=name,
                department_id=id,
                school_id=self.school_id,
            )
