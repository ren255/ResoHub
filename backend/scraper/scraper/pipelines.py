import scrapy
from itemadapter import ItemAdapter
from asgiref.sync import sync_to_async

from core.models import ScrapyItem
from .items import *
from .services.url_manager import url_analyzer, PageType, generate_url
from .services.save_file import TextFile

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
        print(f"processed {item["school_id"]} at SaveDB")
        return item


class Process:
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        item_name = item.__class__.__name__

        if item_name == CollegesOverviewItem.__name__:
            ids = url_analyzer(adapter.get("url_college"))
            item["school_id"] = ids["school_id"]
            print(f"processed {item["school_id"]} at Process")

        if item_name == DepartmentsOverviewItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            item["school_id"] = ids["school_id"]

        if item_name == SubjectCatalogItem.__name__:
            ids = url_analyzer(adapter.get("url_college"))
            item["subject_code"] = ids["subject_code"]

        if item_name == SubjectDetailItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            item["subject_code"] = ids["subject_code"]

        return item


class SchoolID:
    async def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        if not item.__class__.__name__ == CollegesOverviewItem.__name__:
            return item
        file = TextFile(item["scrape_id"], "school_id", "jsonl")
        await file.write_line(json.dumps(adapter.asdict(), ensure_ascii=False))
        print(f"processed {item["school_id"]} at SchoolID")
        return item
