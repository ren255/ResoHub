# %%
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from scrapy.selector import Selector
from core.services import CachedHttpClient

# HTMLを取得
session = CachedHttpClient()
html = session.get("https://www.apple.com/jp/store")

# Scrapyのセレクタを作成
selector = Selector(text=html)

# CSS セレクタでスクレイピング
css_selectors = [
    'a.globalnav-submenu-trigger-link',
    'a.rf-productnav-card-title'
]


# 1つ目のセレクタ: a.globalnav-submenu-trigger-link
elements = selector.css('a.globalnav-submenu-trigger-link')
print("\n[1] globalnav-submenu-trigger-link")
print("-" * 80)
print([elem.css('::attr(href)').get() for elem in elements])
print()


# 2つ目のセレクタ: a.rf-productnav-card-title
elements = selector.css('a.rf-productnav-card-title')
print("\n[2] rf-productnav-card-title")
print("-" * 80)
print([elem.css('::text').get().strip() for elem in elements])
print()

