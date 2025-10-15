from django.db import models
from content.models import User
from django.utils import timezone
import os
import magic
import uuid


def upload_to_uuid(instance, filename):
    """media/{year}/{username}/{uuid}"""
    now = timezone.now()
    ext = filename.split(".")[-1].lower()
    new_filename = f"{uuid.uuid4()}.{ext}"
    username = instance.uploaded_by.username
    return os.path.join("media", str(now.year), username, new_filename)


class File(models.Model):
    """
    ファイル管理モデル
    MinIO (S3互換ストレージ) に保存されるまずは media/{year}/{user_name}/
    """

    # ファイル本体（MinIOに自動保存）
    file = models.FileField(upload_to=upload_to_uuid, verbose_name="ファイル")

    # アップロードユーザー（ユーザー削除時もファイルは保持）
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_files",
        verbose_name="アップロードユーザー",
    )

    # 元のファイル名
    original_filename = models.CharField(max_length=255, verbose_name="元のファイル名")

    # ファイルサイズ（バイト）
    file_size = models.BigIntegerField(default=0, verbose_name="ファイルサイズ")

    # MIMEタイプ（image/png, application/pdf等）
    mine_type = models.CharField(
        max_length=100, blank=True, verbose_name="コンテンツタイプ"
    )

    # 説明（オプショナル）
    description = models.TextField(blank=True, null=True, verbose_name="説明")

    # タイムスタンプ
    uploaded_at = models.DateTimeField(
        auto_now_add=True, verbose_name="アップロード日時"
    )

    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    class Meta:
        ordering = ["-uploaded_at"]
        indexes = [
            models.Index(fields=["-uploaded_at"]),
            models.Index(fields=["uploaded_by"]),
            models.Index(fields=["mine_type"]),
        ]
        verbose_name = "ファイル"
        verbose_name_plural = "ファイル"

    def __str__(self):
        return (
            f"{self.original_filename} ({self.uploaded_at.strftime('%Y-%m-%d %H:%M')})"
        )

    def save(self, *args, **kwargs):
        if not self.original_filename and self.file:
            self.original_filename = os.path.basename(self.file.name)

        if self.file:
            self.file_size = self.file.size
            if not self.mine_type:
                try:
                    self.file.seek(0)
                    mime_type = magic.from_buffer(self.file.read(2048), mime=True)
                    self.mine_type = mime_type
                    self.file.seek(0)
                except Exception:
                    self.mine_type = "application/x"

        super().save(*args, **kwargs)

    def get_file_extension(self):
        """
        ファイル拡張子を取得
        """
        return os.path.splitext(self.original_filename)[1].lower()

    def is_image(self):
        """
        画像ファイルかどうか判定
        """
        return self.mine_type.startswith("image/") if self.mine_type else False

    def get_human_readable_size(self):
        """
        ファイルサイズを人間が読みやすい形式で返す
        例: 1024 → "1.0 KB"
        """
        size = self.file_size
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
