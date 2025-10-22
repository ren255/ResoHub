import scrapy
from scrapy.http.response import Response

from scraper.items import SubjectCatalogItem
from ..services.url_manager import url_analyzer, url_generator, PageType
from ..services.save_file import TextFile

import json
import pandas as pd


class SubjectCatalogSpider(scrapy.Spider):
    name = "subject_catalog"
    allowed_domains = ["syllabus.kosen-k.go.jp"]

    def __init__(self, param1, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.scrape_id = param1

    async def start(self):
        file = TextFile(self.scrape_id, "department_id", "jsonl")
        subjects = await file.read_as_lines()
        for subject in subjects:
            subject = json.loads(subject)
            self.url = url_generator(
                PageType.SUBJECTS,
                school_id=subject["school_id"],
                department_id=subject["department_id"],
                year=2025,
            )
            yield scrapy.Request(self.url, callback=self.parse)

    def parse(self, response: Response):
        df = pd.read_html(response.text, match="学年別週当授業時数")[0]
        skip_first_rows = 4
        column_names = [
            "subject_type",
            "subject_classification",
            "subject_name",
            "subject_code",
            "credit_type",
            "credits",
        ]
        df = df.iloc[skip_first_rows:]
        df.columns = column_names + df.columns.tolist()[len(column_names) :]

        for _, row in df.iterrows():
            # subject urlは無いことがあるため取得しない
            yield SubjectCatalogItem(
                url_source=self.url,
                scrape_id=self.scrape_id,
                name=row["subject_name"],
                subject_code=row["subject_code"],
            )
