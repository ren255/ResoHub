import scrapy


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
