from ..services.url_manager import url_analyzer
import scrapy


class CollegesOverviewItem(scrapy.Item):  # 各高専ごと
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    name = scrapy.Field()
    url_college = scrapy.Field()  # URL解析対象

    def process(self):
        ids = url_analyzer(self.get("url_college"))
        self["school_id"] = ids["school_id"]
