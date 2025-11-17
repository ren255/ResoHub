from django.contrib import admin
from ..models import User, UserSetting, StudentInfo, TeacherInfo


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "school_class__department",
        "student_id",
        "school_class",
        "school_class__admission_year",
    ]
    list_filter = ["school_class__department"]
    search_fields = ["user__name"]


@admin.register(TeacherInfo)
class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "department",
        "subdomain",
    ]
    list_filter = ["department", "subdomain"]
