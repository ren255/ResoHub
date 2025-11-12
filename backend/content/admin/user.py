from django.contrib import admin
from ..models import User, UserSetting, StudentInfo, TeacherInfo


class UserSettingInline(admin.StackedInline):
    model = UserSetting
    extra = 0


class StudentInfoInline(admin.StackedInline):
    model = StudentInfo
    extra = 0


class TeacherInfoInline(admin.StackedInline):
    model = TeacherInfo
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "username",
        "role",
        "email",
        "is_active",
    )

    list_filter = ("is_active", "role")
    search_fields = ("username", "email", "name")
