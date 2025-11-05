from django.contrib import admin
from ..models.subject import SubjectGroupe, Subject


@admin.register(SubjectGroupe)
class SubjectGroupeAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = ["id"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        "school_class__department__name",
        "school_class__department__admission_year",
        "school_class__grade_str",
        "name",
        "code",
        "credits",
        "teachers",
        "textbooks",
    ]
    list_filter = [
        "school_class__department__name",
        "school_class__department__admission_year",
        "name",
        "teachers",
    ]
    search_fields = ["id"]
