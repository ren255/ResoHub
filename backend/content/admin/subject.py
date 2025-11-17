from django.contrib import admin
from django.db.models import Count

from ..models.subject import SubjectGroupe, Subject
from ..models.exam import Exam
from ..models.user_info import TeacherInfo


@admin.register(SubjectGroupe)
class SubjectGroupeAdmin(admin.ModelAdmin):
    list_display = ["id"]
    search_fields = ["id"]


class ExamInline(admin.TabularInline):
    model = Exam
    extra = 0  # no extra empty forms


class TeacherInline(admin.TabularInline):
    model = Subject.teachers.through
    extra = 0


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        "grade_class__school_class__department__name",
        "grade_class__school_class__admission_year",
        "grade_class__grade_str",
        "name",
        "code",
        "credits",
        "teachers_str",
        "teacher_count",
        "textbooks",
        "exam_count",
    ]
    list_filter = [
        "grade_class__school_class__department__name",
        "grade_class__school_class__admission_year",
        "teachers",
        "name",
    ]
    search_fields = ["id"]
    inlines = [ExamInline, TeacherInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_exam_count=Count("exams"))

    def exam_count(self, obj):
        return obj._exam_count

    def teacher_count(self, obj):
        return obj.teachers.count()

    exam_count.admin_order_field = "_exam_count"
    exam_count.short_description = "Exam数"
