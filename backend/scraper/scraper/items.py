# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CollegesOverviewItem(scrapy.Item):  # 各高専ごと
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    name = scrapy.Field()
    url_college = scrapy.Field()  # URL解析対象


class DepartmentsOverviewItem(scrapy.Item):  # 各学科ごと
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    name = scrapy.Field()
    department_url = scrapy.Field()  # URL解析対象


class DepartmentDetailItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    admission_year = scrapy.Field()


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


# class CurriculumMapItem(scrapy.Item):
#     name = scrapy.Field()


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
    is_exam = scrapy.Field()
