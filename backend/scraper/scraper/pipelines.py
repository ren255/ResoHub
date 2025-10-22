import scrapy
from itemadapter import ItemAdapter
from asgiref.sync import sync_to_async

from core.models import ScrapyItem
from .items import *
from .services.url_manager import url_analyzer, PageType, url_generator
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
        return item


class ProcessID:
    def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        item_name = item.__class__.__name__

        if item_name == CollegesOverviewItem.__name__:
            ids = url_analyzer(adapter.get("url_college"))
            adapter["school_id"] = ids["school_id"]
            item.pop("url_college")

        if item_name == DepartmentsOverviewItem.__name__:
            ids = url_analyzer(adapter.get("department_url"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            item.pop("department_url")

        if item_name == SubjectCatalogItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            # subject_codeはtableからとり、tableのあるurlを解析対象

        if item_name == SubjectDetailItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            adapter["subject_code"] = ids["subject_code"]

        item.pop("url_source")
        return item


class SchoolID:
    async def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        if not item.__class__.__name__ == CollegesOverviewItem.__name__:
            return item
        file = TextFile(item["scrape_id"], "school_id", "jsonl")
        await file.write_line(json.dumps(adapter.asdict(), ensure_ascii=False))
        return item


class DepartmentID:
    async def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        if not item.__class__.__name__ == DepartmentsOverviewItem.__name__:
            return item
        file = TextFile(item["scrape_id"], "department_id", "jsonl")
        await file.write_line(json.dumps(adapter.asdict(), ensure_ascii=False))
        return item


class SubjectID:
    async def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        if not item.__class__.__name__ == SubjectCatalogItem.__name__:
            return item
        adapter["name"] = adapter["name"].split("  ")[0]
        file = TextFile(item["scrape_id"], "subject_id", "jsonl")
        await file.write_line(json.dumps(adapter.asdict(), ensure_ascii=False))
        return item
