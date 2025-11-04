from django.contrib import admin
from ..models.exam import ExamGroupe, Exam


@admin.register(ExamGroupe)
class ExamGroupeAdmin(admin.ModelAdmin):
    list_display = ["id", "school_class", "subject_groupe"]
    list_filter = ["school_class", "subject_groupe"]
    search_fields = ["id"]


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ["id", "exam_groupe", "subject", "file"]
    list_filter = ["exam_groupe", "subject"]
    search_fields = ["id"]
