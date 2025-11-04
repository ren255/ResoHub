from django.db import models


class SubjectGroupe(models.Model):
    """教科モデル"""

    unique_id = models.CharField(max_length=100, primary_key=True)

    class Meta:
        db_table = "subject_groupe"
        verbose_name = "教科グループ"
        verbose_name_plural = "教科グループ"


class Subject(models.Model):
    """教科モデル"""

    unique_id = models.CharField(max_length=100, primary_key=True)
    subject_groupe = models.ForeignKey(
        SubjectGroupe,
        on_delete=models.PROTECT,
        db_column="subject_groupe_id",
        verbose_name="教科グループ",
    )

    class Meta:
        db_table = "subject"
        verbose_name = "教科"
        verbose_name_plural = "教科"
