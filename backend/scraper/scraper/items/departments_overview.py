import scrapy


class DepartmentsOverviewItem(scrapy.Item):  # 各学科ごと
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    name = scrapy.Field()
    department_url = scrapy.Field()  # URL解析対象
