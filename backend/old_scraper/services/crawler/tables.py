# %%
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from core.services import CachedHttpClient
import pandas as pd

from ..html_extract import TableExtractor

session = CachedHttpClient()

main_extract = TableExtractor(
    table_match="学年別週当授業時数",
    keep_first_columns=6,
    skip_first_rows=5,
    column_names=[
        "subject_type",
        "subject_classification",
        "subject_name",
        "subject_id",
        "credit_type",
        "credits",
    ],
)

url = "https://syllabus.kosen-k.go.jp/Pages/PublicSubjects?school_id=14&department_id=13&year=2024&lang=ja"

html = session.get(url)
df = main_extract.extract(html)

print(df)
