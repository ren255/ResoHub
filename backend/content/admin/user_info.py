from django.contrib import admin
from ..models import User, UserSetting, StudentInfo, TeacherInfo
from django.db.models import Count


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "school_class__department",
        "student_id",
        "school_class",
        "school_class__admission_year",
    ]
    list_filter = ["school_class__department", "school_class__admission_year"]
    search_fields = ["user__name"]


class SubjectInline(admin.TabularInline):
    model = TeacherInfo.subjects.through
    raw_id_fields = ["subject"]
    extra = 0

    readonly_fields = [
        "subject_type",
        "credits",
        "grade_class",
        "teacher_str",
    ]

    def subject_type(self, instance):
        return instance.subject.subject_type

    def credits(self, instance):
        return instance.subject.credits

    def grade_class(self, instance):
        return instance.subject.grade_class

    def teacher_str(self, instance):
        return instance.subject.teachers_str


@admin.register(TeacherInfo)
class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "department_type",
        "department",
        "subdomain",
        "owner",
        "subject_count",
    ]
    list_filter = ["department", "subdomain"]

    inlines = [SubjectInline]

    def subject_count(self, obj):
        return obj.subjects.count()

    # subject_countをソート可能にする
    subject_count.admin_order_field = "subject_count_annotate"
    subject_count.short_description = "科目数"  # 列のヘッダー名（オプション）

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # annotateでsubject_countを追加
        queryset = queryset.annotate(subject_count_annotate=Count("subjects"))
        return queryset
