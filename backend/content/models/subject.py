from django.db import models
from .organization import SchoolClass


class SubjectGroupe(models.Model):
    """教科モデル"""

    class Meta:
        db_table = "subject_groupe"
        verbose_name = "教科グループ"
        verbose_name_plural = "教科グループ"


class Subject(models.Model):
    """教科モデル"""

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    subject_type = models.CharField(max_length=50)
    credits = models.PositiveIntegerField()
    teachers_str = models.CharField(max_length=300)
    textbooks = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        db_column="class_id",
        related_name="subjects",
    )
    subject_groupe = models.ForeignKey(
        SubjectGroupe,
        on_delete=models.CASCADE,
        db_column="subject_groupe_id",
        related_name="subjects",
        verbose_name="教科グループ",
        null=True,
    )

    class Meta:
        db_table = "subject"
        verbose_name = "教科"
        verbose_name_plural = "教科"

    def __str__(self):
        return f"{self.name} ({self.code})"
