import os
import django

# Django設定の初期化
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from asgiref.sync import sync_to_async
from content.models import (
    User,
    StudentInfo,
    TeacherInfo,
    UserRole,
    School,
    Department,
    SchoolClass,
    Subject,
    SubjectGroupe,
)
from typing import Dict, List
from rapidfuzz.process import cdist
import pandas as pd


import asyncio
from asgiref.sync import sync_to_async


class SubjectUpdate:
    async def process_subjects(self):
        await asyncio.gather(
            self.subject_groupe(),
        )
        print("completed!")

    async def subject_groupe(self):
        @sync_to_async
        def update_groupe():
            SubjectGroupe.objects.all().delete()
            subjects = Subject.objects.prefetch_related("teachers").all()

            # key: (教科名, 講師IDのタプル)
            group_map = {}

            for subject in subjects:
                teacher_ids = tuple(
                    sorted(subject.teachers.values_list("id", flat=True))
                )
                group_key = (subject.name, teacher_ids)
                print(f"key: {group_key}")

                if group_key not in group_map:
                    # 既存グループの中から、名前と講師陣が一致するものを探す
                    groupe = None
                    for existing in SubjectGroupe.objects.filter(
                        name=subject.name
                    ).prefetch_related("teachers"):
                        existing_teacher_ids = tuple(
                            sorted(existing.teachers.values_list("id", flat=True))
                        )
                        if existing_teacher_ids == teacher_ids:
                            groupe = existing
                            break

                    # 一致するグループがなければ新規作成して講師陣を紐付け
                    if groupe is None:
                        groupe = SubjectGroupe.objects.create(name=subject.name)
                        groupe.teachers.set(subject.teachers.all())

                    group_map[group_key] = groupe

                subject.subject_groupe = group_map[group_key]
                subject.save()

        return await update_groupe()


if __name__ == "__main__":
    import asyncio

    processor = SubjectUpdate()
    asyncio.run(processor.process_subjects())
