import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


import pandas as pd
from core.models import TextFileStorage
from core.services import CachedHttpClient
from content.models import User

session = CachedHttpClient()

print("Libraries loaded")

# %%

url = "https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=13&subject_id=0039&year=2024&lang=ja"
url = "https://syllabus.kosen-k.go.jp/Pages/PublicSubjects?school_id=14&department_id=13&year=2024&lang=ja"

html = session.get(url)

tables = pd.read_html(html)
save = "scraper/try/tables"
for i, table in enumerate(tables):
    table.to_csv(f"{save}/{i}.csv")