from django.contrib import admin
from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "original_filename",
        "uploaded_by",
        "get_human_readable_size",
        "content_type",
        "uploaded_at",
    )

    list_filter = (
        "content_type",
        "uploaded_at",
    )

    search_fields = (
        "original_filename",
        "description",
    )

    readonly_fields = (
        "file_size",
        "content_type",
        "uploaded_at",
        "updated_at",
    )

    ordering = ("-uploaded_at",)

    date_hierarchy = "uploaded_at"
