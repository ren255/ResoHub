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

    def get_form(self, request, obj=None, **kwargs):
        """パスワードフィールドを新規作成時に非表示にする"""
        form = super().get_form(request, obj, **kwargs)
        if obj is None:  # 新規作成時のみ
            if "password" in form.base_fields:
                del form.base_fields["password"]
        return form

    def save_model(self, request, obj, form, change):
        """パスワードなしでユーザーを作成可能にする"""
        if not change:  # 新規作成時
            if not obj.password:  # パスワードが空の場合
                obj.set_unusable_password()
        super().save_model(request, obj, form, change)
