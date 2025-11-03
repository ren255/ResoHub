import scrapy
from itemadapter import ItemAdapter
from asgiref.sync import sync_to_async

from core.models import ScrapyItem
from .items import *
from .services.url_manager import url_analyzer, PageType, url_generator
from .services.save_file import TextFile

import json

from time import time


class SaveDB:
    def __init__(self):
        self.timestamps = []
        self.start_time = time()
        self.last_log = time()
        self.log_interval = 10
        self.last_tick = time()

    async def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        data = json.dumps(adapter.asdict(), ensure_ascii=False)
        await sync_to_async(ScrapyItem.objects.create)(
            scrape_id=adapter.get("scrape_id"),
            item_name=item.__class__.__name__,
            spider_name=spider.name,
            data=data,
        )
        self.timestamps.append(time())

        if time() - self.last_log > self.log_interval:
            total = len(self.timestamps)
            last = len(
                [
                    True
                    for timestamp in self.timestamps
                    if time() - timestamp < self.log_interval
                ]
            )
            time_passed = time() - self.last_log
            current_speed = last / time_passed
            speed = total / (time() - self.start_time)
            print(
                f"processed:{total}(+{last}) {current_speed:.2f}items/s({speed:.2f}items/s) in last {time_passed:.2f}s"
            )
            print(f"sample: {data}")
            delay = time_passed - self.log_interval
            if delay > 5:
                print(f"warning!:{delay:.2f}s delay")
            self.last_log = time()

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

        if item_name == DepartmentDetailItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            adapter["admission_year"] = ids["year"]
            item.pop("url_source")

        if item_name == SubjectCatalogItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            adapter["admission_year"] = ids["year"]
            # subject_codeはtableからとり、tableのあるurlを解析対象

        if item_name == SubjectDetailItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            adapter["admission_year"] = ids["year"]
            adapter["subject_code"] = ids["subject_code"]

        item.pop("url_source")
        return item
