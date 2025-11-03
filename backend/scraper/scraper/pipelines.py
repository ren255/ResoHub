import scrapy
from itemadapter import ItemAdapter
from asgiref.sync import sync_to_async

from core.models import ScrapyItem
from .items import *
from .services.url_manager import url_analyzer
from .services.string_utl import extract_year

import json

from time import time


class PerformanceMonitor:
    """パフォーマンス監視とログ出力を担当"""

    def __init__(self, log_interval: int = 10):
        self.timestamps = []
        self.start_time = time()
        self.last_log = time()
        self.log_interval = log_interval

    def record_item(self):
        """アイテム処理を記録"""
        self.timestamps.append(time())

    def should_log(self) -> bool:
        """ログ出力タイミングかどうか"""
        return time() - self.last_log > self.log_interval

    def log_stats(self, sample_data: str):
        """統計情報をログ出力"""
        current_time = time()
        total = len(self.timestamps)

        # 最近の処理数をカウント
        last = sum(
            1
            for timestamp in self.timestamps
            if current_time - timestamp < self.log_interval
        )

        time_passed = current_time - self.last_log
        current_speed = last / time_passed
        overall_speed = total / (current_time - self.start_time)

        print(
            f"processed:{total}(+{last}) {current_speed:.2f}items/s"
            f"({overall_speed:.2f}items/s) in last {time_passed:.2f}s"
        )
        print(f"sample: {sample_data}")

        # 遅延警告
        delay = time_passed - self.log_interval
        if delay > 5:
            print(f"warning!:{delay:.2f}s delay")

        self.last_log = current_time


class SaveDB:
    """データベース保存を担当"""

    def __init__(self):
        self.monitor = PerformanceMonitor(log_interval=10)

    async def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
        adapter = ItemAdapter(item)
        data = json.dumps(adapter.asdict(), ensure_ascii=False)

        # DB保存
        await sync_to_async(ScrapyItem.objects.create)(
            scrape_id=adapter.get("scrape_id"),
            item_name=item.__class__.__name__,
            spider_name=spider.name,
            data=data,
        )

        # パフォーマンス監視
        self.monitor.record_item()
        if self.monitor.should_log():
            self.monitor.log_stats(data)

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
            # item.pop("department_url")

        if item_name == DepartmentDetailItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            adapter["url_year"] = ids["year"]

            adapter["admission_year"] = extract_year(adapter["admission_year"])

        if item_name == SubjectCatalogItem.__name__:
            ids = url_analyzer(adapter.get("subject_url"))
            # subject_codeはtableからとり、tableのあるurlを解析対象
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            adapter["url_year"] = ids["year"]

        if item_name == SubjectDetailItem.__name__:
            ids = url_analyzer(adapter.get("url_source"))
            adapter["school_id"] = ids["school_id"]
            adapter["department_id"] = ids["department_id"]
            adapter["url_year"] = ids["year"]
            adapter["subject_code"] = ids["subject_code"]

        # item.pop("url_source")
        return item
