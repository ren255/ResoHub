from django.contrib import admin
from ..models.organization import School, Department, SchoolClass
from ..models.subject import Subject
from ..models.user_info import StudentInfo


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code"]
    search_fields = ["name", "code"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "school", "name", "admission_year", "url"]
    list_filter = ["school__name", "name", "admission_year"]
    search_fields = ["id"]


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0
    fields = [
        "name",
        "code",
        "subject_type",
        "credits",
        "teachers_str",
        "subject_groupe",
    ]
    readonly_fields = [
        "name",
        "code",
        "subject_type",
        "credits",
        "teachers_str",
        "subject_groupe",
    ]
    show_change_link = True


class StudentsInline(admin.TabularInline):
    model = StudentInfo
    extra = 0
    fields = [
        "user_name",
        "student_id",
        "department",
    ]
    readonly_fields = [
        "user_name",
        "student_id",
        "department",
    ]
    show_change_link = True

    def user_name(self, obj):
        """生徒の名前を表示"""
        if obj.user:
            return obj.user.name
        return "-"

    user_name.short_description = "生徒名"

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "department__school__name",
        "department__name",
        "department__admission_year",
        "grade",
        "grade_str",
        "year",
        "subject_count",
    ]
    list_filter = [
        "grade_str",
        "department__name",
        "department__admission_year",
        "year",
    ]
    search_fields = ["id"]

    inlines = [SubjectInline, StudentsInline]

    def subject_count(self, obj):
        return obj.subjects.count()

    subject_count.short_description = "教科数"
