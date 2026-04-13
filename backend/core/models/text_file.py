from django.db import models
from django.core.exceptions import ValidationError
import re
import os
import magic


class TextFileStorage(models.Model):
    """
    シンプルなテキストファイルストレージモデル
    keyでインデックス化されたファイル情報を管理
    """

    # 主キー
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(
        "content.User", on_delete=models.CASCADE, related_name="text_files"
    )
    key = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        help_text="キーに使用できるのは英数字、(-), (_), (:), (/), (.)のみ",
    )
    body = models.TextField(blank=True, null=True, help_text="ファイルの内容")

    # MIMEタイプ
    mime_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    # ファイルサイズ（バイト）
    file_size = models.IntegerField(default=0)

    # 削除フラグ
    is_deleted = models.BooleanField(default=False)

    # タイムスタンプ
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "text_file_storage"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["key"]),
        ]
        verbose_name = "テキストファイル"
        verbose_name_plural = "テキストファイル一覧"

    def __str__(self):
        return f"{self.key} ({self.id})"

    def get_extension(self):
        """
        keyから.付きファイル拡張子を取得
        """
        _, ext = os.path.splitext(self.key)
        return ext.lower() if ext else ""

    @staticmethod
    def validate_key(key):
        """
        keyのバリデーション

        許可される文字:
        - 英数字 (a-z, A-Z, 0-9)
        - (-), (_), (:), (/), (.)

        禁止事項:
        - (\)などの特殊記号
        - ASCII以外の文字
        - 先頭がドットで始まる文字列
        """
        if not key:
            raise ValidationError("keyは必須です")

        # 許可する文字: 英数字、ハイフン、アンダースコア、コロン、スラッシュ、ドット
        pattern = r"^[a-zA-Z0-9._\-:/]+$"
        if not re.match(pattern, key):
            raise ValidationError(
                "キーに使用できるのは英数字、(-), (_), (:), (/), (.)のみです"
            )

        # 先頭がドットで始まらないようにチェック(隠しファイル防止)
        if key.startswith("."):
            raise ValidationError("keyはドットで始めることはできません")

        return True

    def clean(self):
        """
        モデル保存前のバリデーション
        """
        super().clean()
        self.validate_key(self.key)

    def save(self, *args, **kwargs):
        """
        保存前にバリデーションとサイズ計算を実行
        """
        self.full_clean()
        self.file_size = len(self.body.encode("utf-8")) if self.body else 0
        try:
            buffer = self.body.encode("utf-8")
            mime_type = magic.from_buffer(buffer[:2048], mime=True)
            self.mime_type = mime_type

        except Exception:
            self.mime_type = "application/x"

        super().save(*args, **kwargs)

    def soft_delete(self):
        """
        論理削除を実行
        """
        self.is_deleted = True
        self.save(update_fields=["is_deleted", "updated_at"])

    def restore(self):
        """
        論理削除を復元
        """
        self.is_deleted = False
        self.save(update_fields=["is_deleted", "updated_at"])
