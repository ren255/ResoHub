import scrapy
from ..services.url_manager import url_analyzer


class DepartmentsOverviewItem(scrapy.Item):  # 各学科ごと
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    name = scrapy.Field()
    department_url = scrapy.Field()  # URL解析対象

    def process(self):
        ids = url_analyzer(self.get("department_url"))
        self["school_id"] = ids["school_id"]
        self["department_id"] = ids["department_id"]
