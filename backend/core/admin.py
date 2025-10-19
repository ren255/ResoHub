from django.contrib import admin
from .models import File
from .models import ScrapyItem

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "original_filename",
        "uploaded_by",
        "get_human_readable_size",
        "mine_type",
        "uploaded_at",
    )

    list_filter = (
        "mine_type",
        "uploaded_at",
    )

    search_fields = (
        "original_filename",
        "description",
    )

    readonly_fields = (
        "file_size",
        "mine_type",
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
        'id',
        'key',
        'extension_display',
        'created_by',
        'file_size_display',
        'mine_type',
        'status_display',
        'created_at',
    ]
    
    # フィルター
    list_filter = [
        'is_deleted',
        'mine_type',
        'created_at',
    ]
    
    # 検索
    search_fields = [
        'key',
        'created_by__username',
        'body',
    ]
    
    # 読み取り専用フィールド
    readonly_fields = [
        'id',
        'file_size',
        'created_at',
        'updated_at',
        'extension_display',
    ]
    
    # フィールドセット
    fieldsets = (
        ('基本情報', {
            'fields': ('id', 'key', 'extension_display', 'created_by')
        }),
        ('コンテンツ', {
            'fields': ('body', 'mine_type', 'file_size')
        }),
        ('ステータス', {
            'fields': ('is_deleted',)
        }),
        ('タイムスタンプ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # 1ページあたりの表示件数
    list_per_page = 50
    
    # デフォルトの並び順
    ordering = ['-created_at']
    
    def extension_display(self, obj):
        """拡張子を表示"""
        ext = obj.get_extension()
        return ext if ext else '-'
    extension_display.short_description = '拡張子'
    
    def file_size_display(self, obj):
        """ファイルサイズを読みやすく表示"""
        size = obj.file_size
        if size < 1024:
            return f'{size} B'
        elif size < 1024 * 1024:
            return f'{size / 1024:.1f} KB'
        else:
            return f'{size / (1024 * 1024):.1f} MB'
    file_size_display.short_description = 'サイズ'
    
    def status_display(self, obj):
        """削除状態を視覚的に表示"""
        if obj.is_deleted:
            return format_html(
                '<span style="color: red;">●</span> 削除済み'
            )
        return format_html(
            '<span style="color: green;">●</span> 有効'
        )
    status_display.short_description = 'ステータス'
    
    def has_delete_permission(self, request, obj=None):
        """論理削除を使用するため、物理削除は制限"""
        return request.user.is_superuser
    

@admin.register(ScrapyItem)
class ScrapyItemAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'date', 'data_preview')
    list_filter = ('date',)
    search_fields = ('unique_id', 'data')
    readonly_fields = ('date',)
    ordering = ('-date',)
    
    def data_preview(self, obj):
        """データの最初の100文字を表示"""
        return obj.data[:100] + '...' if len(obj.data) > 100 else obj.data
    data_preview.short_description = 'Data Preview'
    
    fieldsets = (
        ('基本情報', {
            'fields': ('unique_id', 'date')
        }),
        ('クロールデータ', {
            'fields': ('data',),
            'classes': ('wide',)
        }),
    )