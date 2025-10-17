# %%
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from core.services import CachedHttpClient
from time import time
from pprint import pprint

from ..services.selector_extractor import (
    ElementAttrEnum,
    InstructionField,
    CssSelectExtractor,
)

session = CachedHttpClient()


html_main = session.get(
    "https://syllabus.kosen-k.go.jp/Pages/PublicSubjects?school_id=14&department_id=13&year=2024&lang=ja"
)
html = html = session.get(
    "https://syllabus.kosen-k.go.jp/Pages/PublicSyllabus?school_id=14&department_id=13&subject_id=0026&year=2024&lang=ja"
)


meta_info_select = (
    "#MainContent_SubjectSyllabus_UpdatePanelSyllabus > div > .no-padding td"
)
instructions = {
    "subject_name": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=2,
    ),
    "subject_number": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=3,
    ),
    "class_format": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=5,
    ),
    "year_started": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=1,
    ),
    "subject_name": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=1,
    ),
    "subject_name": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=1,
    ),
    "subject_name": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=1,
    ),
    "subject_name": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=1,
    ),
    "subject_name": InstructionField(
        css_selector=meta_info_select,
        attr=ElementAttrEnum.TEXT,
        index=1,
    ),
}

extractor = CssSelectExtractor(instructions)

start = time()
result = extractor.extract(html)
end = time()

pprint(result)
print("Elapsed time:", end - start, "seconds")
