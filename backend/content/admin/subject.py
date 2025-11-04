from django.contrib import admin
from ..models.subject import SubjectGroupe, Subject


@admin.register(SubjectGroupe)
class SubjectGroupeAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = ["id"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id", "subject_groupe"]
    list_filter = ["subject_groupe"]
    search_fields = ["id"]
