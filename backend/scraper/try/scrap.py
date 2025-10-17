# %%
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from core.services import CachedHttpClient

from ..services.selector_extractor import (
    ElementAttrEnum,
    InstructionField,
    CssSelectExtractor,
)

# 抽出指示の作成
instructions = {
    "links": InstructionField(
        css_selector="a.globalnav-submenu-trigger-link", attr=ElementAttrEnum.HREF
    ),
    "texts": InstructionField(
        css_selector="a.rf-productnav-card-title", attr=ElementAttrEnum.TEXT
    ),
}

# CssSelectExtractor の初期化
extractor = CssSelectExtractor(instructions)

# HTMLの取得（元のコードの通り）
session = CachedHttpClient()
html = session.get("https://www.apple.com/jp/store")

from time import time

start = time()
result = extractor.extract(html)
end = time()

print("Extraction result:", result)
print("Elapsed time:", end - start, "seconds")


from pprint import pprint

pprint(result)
