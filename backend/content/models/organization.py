from django.db import models


class School(models.Model):
    """学校モデル"""

    name = models.CharField(max_length=200, verbose_name="学校名")
    code = models.CharField(max_length=50, verbose_name="学校コード")
    # address = models.CharField(max_length=100, verbose_name="学校住所")
    # region = models.CharField(max_length=20, verbose_name="地域区分")

    class Meta:
        db_table = "school"
        verbose_name = "学校"
        verbose_name_plural = "学校"

    def __str__(self):
        return self.name


class Department(models.Model):
    """学部モデル XXXX年度入学XX学部"""

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        db_column="school_id",
        related_name="departments",
        verbose_name="学校",
    )
    admission_year = models.IntegerField(verbose_name="入学年度")

    class Meta:
        db_table = "department"
        verbose_name = "学部"
        verbose_name_plural = "学部"

    def __str__(self):
        return f"{self.school.name} - {self.admission_year}"


class SchoolClass(models.Model):
    """クラスモデル X学年(XXXX年度入学XX学部)"""

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        db_column="department_id",
        related_name="classes",
        verbose_name="学部",
    )
    grade = models.IntegerField(verbose_name="学年")

    class Meta:
        db_table = "class"
        verbose_name = "クラス"
        verbose_name_plural = "クラス"

    def __str__(self):
        return f"{self.department} - {self.grade}年"
