from core.models import ScrapyItem
from asgiref.sync import sync_to_async
from typing import List


class ItemCollection:
    def __init__(self, scrape_id, item_name):
        self.scrape_id = scrape_id
        self.item_name = item_name
        self.ids = []
        self._storage = ScrapyItem

    async def update_ids(self) -> List[str]:
        """prefix配下の全keyを取得してself.keysに格納"""
        self.ids = await sync_to_async(list)(
            self._storage.objects.filter(
                scrape_id=self.scrape_id,
                item_name=self.item_name,
            )
            .order_by("unique_id")
            .values_list("unique_id", flat=True)
        )
        return self.ids

    async def get_data(self) -> List[str]:
        """self.keys配下の全bodyをリストで返す"""
        await self.update_ids()
        if not self.ids:
            return []

        data = await sync_to_async(list)(
            self._storage.objects.filter(unique_id__in=self.ids)
            .order_by("unique_id")
            .values_list("data", flat=True)
        )
        return data

    async def delete_all(self) -> None:
        """self.keys配下を全削除"""
        await self.update_ids()
        if not self.ids:
            return

        await sync_to_async(
            self._storage.objects.filter(unique_id__in=self.ids).delete
        )()
        self.ids = []
