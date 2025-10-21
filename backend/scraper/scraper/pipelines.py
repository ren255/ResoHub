import scrapy
from itemadapter import ItemAdapter
from asgiref.sync import sync_to_async

from core.models import ScrapyItem, TextFileStorage
from scraper.items import *

import json


class SaveDB:
    async def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)

        await sync_to_async(ScrapyItem.objects.create)(
            scrape_id=adapter.get("scrape_id"),
            item_name=item.__class__.__name__,
            spider_name=spider.name,
            data=json.dumps(adapter.asdict(), ensure_ascii=False),
        )

        return item


class Process:
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        item_name = item.__class__.__name__

        if item_name == CollegesOverviewItem.__name__:
            pass

        if item_name == DepartmentsOverviewItem.__name__:
            pass

        if item_name == SubjectCatalogItem.__name__:
            pass

        if item_name == SubjectDetailItem.__name__:
            pass

        return item
