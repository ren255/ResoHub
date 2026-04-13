from django.db import models
from .organization import SchoolClass, School, Department, SyllabusDepartment
from .subject import Subject


class UserSetting(models.Model):
    """各userごとのカスタムなどのprofile保存"""

    user = models.OneToOneField(
        "content.User", on_delete=models.CASCADE, related_name="user_setting"
    )

    class Meta:
        db_table = "user_setting"
        verbose_name = "ユーザー設定"
        verbose_name_plural = "ユーザー設定"

    def __str__(self):
        return f"{self.user.username}の設定"


class StudentInfo(models.Model):
    """生徒固有情報を保存"""

    user = models.OneToOneField(
        "content.User", on_delete=models.CASCADE, related_name="student_info"
    )
    student_id = models.CharField(max_length=10)
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        related_name="students",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "student_info"
        verbose_name = "生徒情報"
        verbose_name_plural = "生徒情報"

    def __str__(self):
        return f"{self.user} ({self.student_id})"


class TeacherInfo(models.Model):
    """教師固有情報を保存"""

    user = models.OneToOneField(
        "content.User", on_delete=models.CASCADE, related_name="teacher_info"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        null=True,
    )
    department_type = models.CharField(max_length=20, default="")
    owner = models.BooleanField(default=False)
    subdomain = models.CharField(max_length=10)
    subjects = models.ManyToManyField(
        Subject,
        related_name="teachers",
        verbose_name="担当教科",
    )

    class Meta:
        db_table = "teacher_info"
        verbose_name = "教師情報"
        verbose_name_plural = "教師情報"

    def __str__(self):
        return f"{self.department_type}学部 {self.user.username.split()[0]}先生"
