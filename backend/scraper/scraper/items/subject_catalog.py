import scrapy
from ..services.url_manager import url_analyzer


class SubjectCatalogItem(scrapy.Item):
    url_source = scrapy.Field()
    subject_url = scrapy.Field()  # URL解析対象
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    url_year = scrapy.Field()  # URLより
    subject_code = scrapy.Field()  # tableより
    name = scrapy.Field()
    subject_type = scrapy.Field()
    subject_classification = scrapy.Field()
    subject_name = scrapy.Field()
    subject_id = scrapy.Field()
    credit_type = scrapy.Field()
    credits = scrapy.Field()

    def process(self):
        ids = url_analyzer(self.get("subject_url"))
        # subject_codeはtableからとり、tableのあるurlを解析対象
        self["school_id"] = ids["school_id"]
        self["department_id"] = ids["department_id"]
        self["url_year"] = ids["year"]
