from django.db import models
from .subject import Subject, SubjectGroupe
from core.models import TextFileStorage


class ExamGroupe(models.Model):
    """試験モデル"""

    unique_id = models.CharField(max_length=100, primary_key=True)
    subject_groupe = models.ForeignKey(
        SubjectGroupe,
        on_delete=models.PROTECT,
        db_column="subject_groupe_id",
        verbose_name="教科グループ",
    )

    class Meta:
        db_table = "exam_groupe"
        verbose_name = "試験グループ"
        verbose_name_plural = "試験グループ"


class Exam(models.Model):
    """試験モデル"""

    unique_id = models.CharField(max_length=100, primary_key=True)
    exam_groupe = models.ForeignKey(
        ExamGroupe,
        on_delete=models.PROTECT,
        db_column="exam_groupe_id",
        verbose_name="試験グループ",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        db_column="subject_id",
        verbose_name="教科",
    )
    file = models.ForeignKey(
        TextFileStorage,
        on_delete=models.PROTECT,
        db_column="file_id",
        verbose_name="ファイル",
    )

    class Meta:
        db_table = "exam"
        verbose_name = "試験"
        verbose_name_plural = "試験"
