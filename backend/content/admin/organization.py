from django.contrib import admin
from ..models.organization import (
    School,
    Department,
    SchoolClass,
    SyllabusDepartment,
    GradeClass,
)
from ..models.subject import Subject
from ..models.user_info import StudentInfo


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code"]
    search_fields = ["name", "code"]


@admin.register(SyllabusDepartment)
class SyllabusDepartmentAdmin(admin.ModelAdmin):
    list_display = ["school", "name", "code", "admission_year", "department"]
    list_filter = ["school", "name", "admission_year", "department"]
    search_fields = ["name"]


class StudentsInline(admin.TabularInline):
    model = StudentInfo
    extra = 0
    fields = ["user_name", "student_id"]
    readonly_fields = ["user_name", "student_id"]
    # fk_name = "school_class__department"

    def user_name(self, obj):
        """生徒の名前を表示"""
        if obj.user:
            return obj.user.name
        return ""

    user_name.short_description = "生徒名"

    def student_id(self, obj):
        """学籍番号を表示"""
        return obj.student_id if obj.student_id else "-"

    student_id.short_description = "学籍番号"

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["school", "name"]
    list_filter = ["school", "name"]
    search_fields = ["name"]

    # inlines = [StudentsInline]


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0
    fields = [
        "name",
        "code",
        "subject_type",
        "credits",
        "teachers_str",
    ]
    readonly_fields = [
        "name",
        "code",
        "subject_type",
        "credits",
        "teachers_str",
    ]


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = [
        "department__school__name",
        "department__name",
        "admission_year",
        "student_count",
    ]
    list_filter = [
        "department__name",
        "admission_year",
    ]
    search_fields = ["department__name"]

    inlines = [StudentsInline]

    def student_count(self, obj):
        """この学科に所属する生徒数を表示"""
        return obj.students.count()

    student_count.short_description = "生徒数"


@admin.register(GradeClass)
class GradeClassAdmin(admin.ModelAdmin):
    list_display = [
        "school_class",
        "subject_count",
        "grade_str",
        "grade",
        "year",
    ]
    list_filter = [
        "school_class__department__name",
        "school_class__admission_year",
        "grade_str",
        "grade",
        "year",
    ]
    search_fields = [
        "school_class__department__name",
    ]

    inlines = [SubjectInline]

    def subject_count(self, obj):
        return obj.subjects.count()

    subject_count.short_description = "教科数"
