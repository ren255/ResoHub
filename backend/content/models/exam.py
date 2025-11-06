from django.db import models
from .organization import SchoolClass
from .subject import Subject, SubjectGroupe
from core.models import TextFileStorage


class ExamGroupe(models.Model):
    """試験モデル"""

    school_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.CASCADE,
        db_column="school_class_id",
        verbose_name="教科グループ",
    )
    subject_groupe = models.ForeignKey(
        SubjectGroupe,
        on_delete=models.CASCADE,
        db_column="subject_groupe_id",
        verbose_name="教科グループ",
    )

    class Meta:
        db_table = "exam_groupe"
        verbose_name = "試験グループ"
        verbose_name_plural = "試験グループ"


class Exam(models.Model):
    """試験モデル"""

    url = models.CharField(max_length=200)
    quarter = models.PositiveIntegerField()
    week = models.PositiveIntegerField()
    content = models.CharField(max_length=500)
    goal = models.CharField(max_length=500)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        db_column="subject_id",
        related_name="exams",
        verbose_name="教科",
    )
    exam_groupe = models.ForeignKey(
        ExamGroupe,
        on_delete=models.CASCADE,
        db_column="exam_groupe_id",
        related_name="exams",
        verbose_name="試験グループ",
        null=True,
    )
    file = models.ForeignKey(
        TextFileStorage,
        on_delete=models.CASCADE,
        db_column="file_id",
        verbose_name="ファイル",
        null=True,
    )

    class Meta:
        db_table = "exam"
        verbose_name = "試験"
        verbose_name_plural = "試験"
