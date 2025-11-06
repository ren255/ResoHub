from django.contrib import admin
from ..models.subject import SubjectGroupe, Subject
from ..models.exam import Exam


@admin.register(SubjectGroupe)
class SubjectGroupeAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = ["id"]


class ExamInline(admin.TabularInline):
    model = Exam
    extra = 0  # no extra empty forms


from django.db.models import Count


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        "school_class__department__name",
        "school_class__department__admission_year",
        "school_class__grade_str",
        "name",
        "code",
        "credits",
        "teachers_str",
        "textbooks",
        "exam_count",
    ]
    list_filter = [
        "school_class__department__name",
        "school_class__department__admission_year",
        "name",
        "teachers_str",
    ]
    search_fields = ["id"]
    inlines = [ExamInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_exam_count=Count("exams"))

    def exam_count(self, obj):
        return obj._exam_count

    exam_count.admin_order_field = "_exam_count"
    exam_count.short_description = "Exam数"
