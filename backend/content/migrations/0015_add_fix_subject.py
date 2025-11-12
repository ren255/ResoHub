# manualy

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0014_schoolclass_grade_str_subject_code_subject_credits_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="subject_type",
            field=models.CharField(default="", max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="teachers",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="textbooks",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subject",
            name="url",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
