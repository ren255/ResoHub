# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CollegesOverviewItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    name = scrapy.Field()
    url_college = scrapy.Field()
    school_id = scrapy.Field()


class DepartmentsOverviewItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    department_id = scrapy.Field()  # URLより
    name = scrapy.Field()
    url_subject_catalog = scrapy.Field()
    url_curriculum_map = scrapy.Field()


class SubjectCatalogItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    subject_code = scrapy.Field()  # URLより
    name = scrapy.Field()
    url_subject = scrapy.Field()
    subject_type = scrapy.Field()
    subject_classification = scrapy.Field()
    subject_name = scrapy.Field()
    subject_id = scrapy.Field()
    credit_type = scrapy.Field()
    credits = scrapy.Field()


# class CurriculumMapItem(scrapy.Item):
#     name = scrapy.Field()


class SubjectDetailItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    subject_code = scrapy.Field()  # URLより
    name = scrapy.Field()
    subject_type = scrapy.Field()
    subject_classification = scrapy.Field()
    subject_name = scrapy.Field()
    subject_id = scrapy.Field()
    credit_type = scrapy.Field()
    credits = scrapy.Field()
    # new
    year = scrapy.Field()
    grade = scrapy.Field()
    teachers = scrapy.Field()
    textbooks = scrapy.Field()
    week_hour = scrapy.Field()
    open_period = scrapy.Field()


class SubjectContentItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    subject_code = scrapy.Field()  # URLより
    term = scrapy.Field()
    quarter = scrapy.Field()
    week = scrapy.Field()
    content = scrapy.Field()
    goal = scrapy.Field()
