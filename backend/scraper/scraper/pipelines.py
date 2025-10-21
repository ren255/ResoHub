from itemadapter import ItemAdapter
from core.models import ScrapyItem
import json
from asgiref.sync import sync_to_async
import scrapy


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
