from django.contrib import admin
from ..models.organization import School, Department, SchoolClass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code"]
    search_fields = ["name", "code"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "school", "name", "admission_year", "url"]
    list_filter = ["school__name", "name", "admission_year"]
    search_fields = ["id"]


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
    ]
    list_filter = [
        "grade_str",
        "department__name",
        "department__admission_year",
        "year",
    ]
    search_fields = ["id"]

    readonly_fields = ("display_subjects",)

    def display_subjects(self, obj):
        return "\n".join(
            f"{subject.name}  : {subject.teachers}" for subject in obj.subjects.all()
        )

    display_subjects.short_description = "Subjects"
