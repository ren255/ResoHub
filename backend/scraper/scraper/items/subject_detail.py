import scrapy


class SubjectDetailItem(scrapy.Item):
    url_source = scrapy.Field()  # URL解析対象
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    url_year = scrapy.Field()  # URLより
    subject_code = scrapy.Field()  # URLより
    subject_type = scrapy.Field()
    subject_classification = scrapy.Field()
    subject_name = scrapy.Field()
    credit_type = scrapy.Field()
    credits = scrapy.Field()
    # new
    admission_year = scrapy.Field()
    grade = scrapy.Field()
    teachers = scrapy.Field()
    textbooks = scrapy.Field()
    week_hour = scrapy.Field()
    open_period = scrapy.Field()


class SubjectContentItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    quarter = scrapy.Field()
    week = scrapy.Field()
    content = scrapy.Field()
    goal = scrapy.Field()
