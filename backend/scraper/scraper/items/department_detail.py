import scrapy
from ..services.url_manager import url_analyzer


class DepartmentDetailItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    name = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    admission_year = scrapy.Field()

    def process(self):
        ids = url_analyzer(self.get("url_source"))
        self["school_id"] = ids["school_id"]
        self["department_id"] = ids["department_id"]
        self["admission_year"] = ids["year"]
