import scrapy
from ..services.url_manager import url_analyzer
from ..services.string_utl import extract_year
import re


class SubjectDetailItem(scrapy.Item):
    url_source = scrapy.Field()  # URL解析対象
    scrape_id = scrapy.Field()
    school_id = scrapy.Field()  # URLより
    department_id = scrapy.Field()  # URLより
    url_year = scrapy.Field()  # 入学年
    subject_code = scrapy.Field()  # URLより
    subject_type = scrapy.Field()
    subject_classification = scrapy.Field()
    subject_name = scrapy.Field()
    credit_type = scrapy.Field()
    credits = scrapy.Field()
    # new
    academic_year = scrapy.Field()  # 開講年度(実施年度)
    grade_str = scrapy.Field()
    fixed_grade = scrapy.Field()
    teachers = scrapy.Field()
    textbooks = scrapy.Field()
    week_hour = scrapy.Field()
    open_period = scrapy.Field()
    # year = scrapy.Field() 削除(admission_yearがacademic_yearになりurl_yearが入学年であったため)

    def process(self):
        ids = url_analyzer(self.get("url_source"))
        self["school_id"] = ids["school_id"]
        self["department_id"] = ids["department_id"]
        self["url_year"] = ids["year"]
        self["subject_code"] = ids["subject_code"] if ids["subject_code"] else ""
        self["textbooks"] = self["textbooks"] if self["textbooks"] else ""

        self["academic_year"] = extract_year(self["academic_year"])

        try:
            self["fixed_grade"] = int(self["grade_str"])
            # self["year"] = self["admission_year"] + self["fixed_grade"] - 1
        except ValueError:
            # 専攻科生 "専2" admission_yearはresetされる
            self["fixed_grade"] = int(self["grade_str"][1:]) + 5
            # self["year"] = self["admission_year"] + int(self["grade_str"][1:]) - 1


class SubjectContentItem(scrapy.Item):
    url_source = scrapy.Field()
    scrape_id = scrapy.Field()
    quarter = scrapy.Field()
    week = scrapy.Field()
    content = scrapy.Field()
    goal = scrapy.Field()
    is_exam = scrapy.Field()

    def process(self):
        # data exportでurl_source経由でsubject detail より所属を見つけるためids無し
        if "試験" in self["content"]:
            self["is_exam"] = True
