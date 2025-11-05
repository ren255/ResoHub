import scrapy


class DepartmentDetailItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    name = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    admission_year = scrapy.Field()
