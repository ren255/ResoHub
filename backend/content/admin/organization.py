from django.contrib import admin
from ..models.organization import School, Department, SchoolClass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code"]
    search_fields = ["name", "code"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "school", "name", "admission_year", "url"]
    list_filter = ["name", "admission_year"]
    search_fields = ["id"]


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ["id", "department", "grade"]
    list_filter = ["grade", "department"]
    search_fields = ["id"]
