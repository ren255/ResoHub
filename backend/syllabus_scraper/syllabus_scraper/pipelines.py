# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from core.models import ScrapyItem
import json
from asgiref.sync import sync_to_async


class SyllabusScraperPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get("unique_id"),
        )

    async def close_spider(self, spider):
        # Wrap the Django ORM operations in sync_to_async
        await sync_to_async(self._save_items)()

    def _save_items(self):
        """Synchronous method to save items"""
        item = ScrapyItem()
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):
        self.items.append(item["url"])
        return item
