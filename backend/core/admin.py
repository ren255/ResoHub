from django.contrib import admin
from .models import File
from .models import ScrapyItem


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "original_filename",
        "uploaded_by",
        "get_human_readable_size",
        "mime_type",
        "uploaded_at",
    )

    list_filter = (
        "mime_type",
        "uploaded_at",
    )

    search_fields = (
        "original_filename",
        "description",
    )

    readonly_fields = (
        "file_size",
        "mime_type",
        "uploaded_at",
        "updated_at",
    )

    ordering = ("-uploaded_at",)

    date_hierarchy = "uploaded_at"


from django.contrib import admin
from django.utils.html import format_html
from .models import TextFileStorage


@admin.register(TextFileStorage)
class TextFileStorageAdmin(admin.ModelAdmin):
    """
    TextFileStorageのシンプルな管理画面
    """

    # リスト表示
    list_display = [
        "id",
        "key",
        "extension_display",
        # "created_by__username",
        "file_size_display",
        "mime_type",
        "status_display",
        "created_at",
    ]

    # フィルター
    list_filter = [
        "is_deleted",
        "mime_type",
        "created_at",
    ]

    # 検索
    search_fields = [
        "key",
        # "created_by__username",
        "body",
    ]

    # 読み取り専用フィールド
    readonly_fields = [
        "id",
        "file_size",
        "created_at",
        "updated_at",
        "extension_display",
    ]

    # フィールドセット
    fieldsets = (
        ("基本情報", {"fields": ("id", "key", "extension_display", "created_by")}),
        ("コンテンツ", {"fields": ("body", "mime_type", "file_size")}),
        ("ステータス", {"fields": ("is_deleted",)}),
        (
            "タイムスタンプ",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )

    # 1ページあたりの表示件数
    list_per_page = 50

    # デフォルトの並び順
    ordering = ["-created_at"]

    def extension_display(self, obj):
        """拡張子を表示"""
        ext = obj.get_extension()
        return ext if ext else "-"

    extension_display.short_description = "拡張子"

    def file_size_display(self, obj):
        """ファイルサイズを読みやすく表示"""
        size = obj.file_size
        if size < 1024:
            return f"{size} B"
        elif size < 1024 * 1024:
            return f"{size / 1024:.1f} KB"
        else:
            return f"{size / (1024 * 1024):.1f} MB"

    file_size_display.short_description = "サイズ"

    def status_display(self, obj):
        if obj.is_deleted:
            return format_html(
                '<span style="color: {};">●</span> {}', "red", "削除済み"
            )
        return format_html('<span style="color: {};">●</span> {}', "green", "有効")

    status_display.short_description = "ステータス"

    def has_delete_permission(self, request, obj=None):
        """論理削除を使用するため、物理削除は制限"""
        return request.user.is_superuser


import json
from django.utils.html import format_html


@admin.register(ScrapyItem)
class ScrapyItemAdmin(admin.ModelAdmin):
    list_display = ("item_name", "spider_name", "data_preview")
    list_filter = ("item_name", "spider_name", "scrape_id")
    search_fields = ("data",)
    ordering = ("date",)

    def has_add_permission(self, request):
        """追加権限を無効化"""
        return False

    def has_change_permission(self, request, obj=None):
        """変更権限を無効化"""
        return False

    def data_preview(self, obj):
        """データの最初の100文字を表示"""
        return obj.data[:100] + "..." if len(obj.data) > 100 else obj.data

    data_preview.short_description = "Data Preview"

    def data_formatted(self, obj):
        """JSONデータを整形して表示"""
        try:
            # JSONとしてパース
            data_dict = json.loads(obj.data) if isinstance(obj.data, str) else obj.data
            # インデント付きで整形
            formatted = json.dumps(data_dict, indent=2, ensure_ascii=False)
            # HTMLのpreタグで表示
            return format_html(
                '<pre style="white-space: pre-wrap; word-wrap: break-word;">{}</pre>',
                formatted,
            )
        except (json.JSONDecodeError, TypeError):
            # JSONでない場合はそのまま表示
            return format_html("<pre>{}</pre>", obj.data)

    data_formatted.short_description = "Data (Formatted)"

    fieldsets = (
        (
            "基本情報",
            {"fields": ("unique_id", "scrape_id", "item_name", "spider_name", "date")},
        ),
        ("クロールデータ", {"fields": ("data_formatted",), "classes": ("wide",)}),
    )

    readonly_fields = ("data_formatted",)
