from core.models import TextFileStorage
from content.models import User
from django.db import transaction
from channels.db import database_sync_to_async

from asgiref.sync import sync_to_async
import pandas as pd
from io import StringIO


class TextFile:
    def __init__(self, scrape_id: str, file_type: str, extension: str):
        self.scrape_id = scrape_id
        self.file_type = file_type
        self.extension = extension
        self._created_by = None
        self._storage = TextFileStorage

    async def _get_created_by(self):
        """created_byを遅延初期化"""
        if self._created_by is None:
            self._created_by = await sync_to_async(User.objects.get)(username="scrapy")
        return self._created_by

    @property
    def key(self) -> str:
        """NoSQL用key生成"""
        return f"{self.scrape_id}/{self.file_type}.{self.extension}"

    @database_sync_to_async
    def _get_or_create_instance(self, created_by):
        with transaction.atomic():
            instance, _ = self._storage.objects.get_or_create(
                key=self.key, defaults={"created_by": created_by, "body": ""}
            )
        return instance

    async def _get_instance(self):
        created_by = await self._get_created_by()
        instance = await self._get_or_create_instance(created_by)
        return instance

    async def _get_body(self) -> str:
        """bodyを取得"""
        try:
            instance = await self._get_instance()
            return instance.body or ""
        except self._storage.DoesNotExist:
            return ""

    async def read_as_lines(self) -> list[str]:
        """行単位でリストとして読み込む"""
        body = await self._get_body()
        return [line for line in body.strip().split("\n") if line]

    async def read_as_dataframe(self) -> pd.DataFrame:
        """テーブル形式としてDataFrameで読み込む"""
        body = await self._get_body()
        delimiter = "\t" if self.extension == "tsv" else ","
        return pd.read_csv(StringIO(body), delimiter=delimiter)

    async def read_file(self) -> str:
        """生テキストとして読み込む"""
        return await self._get_body()

    async def write_file(self, text: str) -> None:
        """ファイル全体を書き込む"""
        instance = await self._get_instance()
        instance.body = text
        await sync_to_async(instance.save)(update_fields=["body"])

    async def write_line(self, line: str) -> None:
        """行を追記する（取得→更新を排他ロック）"""
        # ① 非同期でインスタンスの pk を取得（既にある self._get_instance を利用）
        instance = await self._get_instance()
        pk = instance.pk

        # ② 同期関数でトランザクション＋select_for_update を行う
        await self._atomic_append_by_pk(self._storage, pk, line)

    @database_sync_to_async
    def _atomic_append_by_pk(self, storage_model, pk, line):
        # ここは同期コード。transaction.atomic は同期コンテキストマネージャ。
        with transaction.atomic():
            # select_for_update() で行ロックを取得
            inst = storage_model.objects.select_for_update().get(pk=pk)

            body = inst.body or ""
            inst.body = (body + line + "\n") if body else (line + "\n")

            # 必要なフィールドだけ更新して保存
            inst.save(update_fields=["body", "mime_type", "file_size"])

    async def exists(self) -> bool:
        """ファイルが存在するか確認"""
        return await sync_to_async(self._storage.objects.filter(key=self.key).exists)()

    async def delete(self) -> None:
        """ファイルを削除"""
        await sync_to_async(self._storage.objects.filter(key=self.key).delete)()
