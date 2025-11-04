from django.contrib import admin
from ..models.subject import SubjectGroupe, Subject


@admin.register(SubjectGroupe)
class SubjectGroupeAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = ["id"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "code",
        "school_class__grade_str",
        "school_class",
        "credits",
        "url",
    ]
    list_filter = [
        "school_class__department__name",
        "school_class__department__admission_year",
        "name",
    ]
    search_fields = ["id"]
