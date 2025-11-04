from django.contrib import admin
from ..models.subject import SubjectGroupe, Subject


@admin.register(SubjectGroupe)
class SubjectGroupeAdmin(admin.ModelAdmin):
    list_display = ["unique_id"]
    search_fields = ["unique_id"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["unique_id", "subject_groupe"]
    list_filter = ["subject_groupe"]
    search_fields = ["unique_id"]
