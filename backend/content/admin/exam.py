from django.contrib import admin
from ..models.exam import ExamGroupe, Exam


@admin.register(ExamGroupe)
class ExamGroupeAdmin(admin.ModelAdmin):
    list_display = ["subject_groupe"]
    list_filter = ["subject_groupe"]
    search_fields = ["id"]


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = [
        "exam_groupe",
        "subject",
        "quarter",
        "week",
        "content",
        "goal",
    ]
    list_filter = ["exam_groupe", "subject"]
    search_fields = ["id"]
