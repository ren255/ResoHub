from core.models import TextFileStorage
from content.models import User
from django.db import transaction
from channels.db import database_sync_to_async

from asgiref.sync import sync_to_async
import pandas as pd
from io import StringIO
from typing import List
import sys


class TextFile:
    def __init__(
        self, scrape_id: str, file_type: str, extension: str, worker_id: str = None
    ):
        self.scrape_id = scrape_id
        self.file_type = file_type
        self.extension = extension
        self.worker_id = worker_id
        self._created_by = None
        self._storage = TextFileStorage

    async def _get_created_by(self):
        """created_byを遅延初期化"""
        if self._created_by is None:
            try:
                self._created_by = await sync_to_async(User.objects.get)(
                    username="scrapy"
                )
            except User.DoesNotExist:
                print("scrapy User not found")
                sys.exit()
        return self._created_by

    @property
    def key(self) -> str:
        if self.worker_id:
            return (
                f"{self.scrape_id}/{self.file_type}/{self.worker_id}.{self.extension}"
            )
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

        if self.extension == "jsonl":
            return pd.read_json(StringIO(body), lines=True)

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


class TextFileCollection:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.keys = []
        self._storage = TextFileStorage

    async def update_keys(self) -> List[str]:
        """prefix配下の全keyを取得してself.keysに格納"""
        self.keys = await sync_to_async(list)(
            self._storage.objects.filter(key__startswith=self.prefix)
            .order_by("key")
            .values_list("key", flat=True)
        )
        return self.keys

    async def get_bodies(self) -> List[str]:
        """self.keys配下の全bodyをリストで返す"""
        if not self.keys:
            return []

        bodies = await sync_to_async(list)(
            self._storage.objects.filter(key__in=self.keys)
            .order_by("key")
            .values_list("body", flat=True)
        )
        return bodies

    async def delete_all(self) -> None:
        """self.keys配下を全削除"""
        if not self.keys:
            return

        await sync_to_async(self._storage.objects.filter(key__in=self.keys).delete)()
        self.keys = []

    async def bulk_update_bodies(self, new_bodies: List[str]) -> None:
        """self.keys配下のbodyを一括更新"""
        if not self.keys or len(self.keys) != len(new_bodies):
            raise ValueError("keys and bodies length mismatch")

        @database_sync_to_async
        def _bulk_update():
            instances = list(
                self._storage.objects.filter(key__in=self.keys).order_by("key")
            )

            for instance, new_body in zip(instances, new_bodies):
                instance.body = new_body

            self._storage.objects.bulk_update(
                instances, fields=["body", "mime_type", "file_size"]
            )

        await _bulk_update()
