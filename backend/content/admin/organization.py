from django.contrib import admin
from ..models.organization import School, Department, SchoolClass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["unique_id", "name", "code"]
    search_fields = ["name", "code"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["unique_id", "school", "admission_year"]
    list_filter = ["admission_year", "school"]
    search_fields = ["unique_id"]


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ["unique_id", "department", "grade"]
    list_filter = ["grade", "department"]
    search_fields = ["unique_id"]
