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
)
from typing import Dict, List
from rapidfuzz.process import cdist
import pandas as pd


class UserProcessor:
    async def process_users(self):
        """学生と教師の詳細情報を更新"""
        await asyncio.gather(
            self.process_students(),
            self.process_teachers(),
        )
        print("User details processing completed!")

    def _parse_student_id(self, student_id: str) -> tuple[str, int] | None:
        """学生IDから学科と入学年度を解析"""
        if not student_id or len(student_id) < 3:
            return None

        department_id = student_id[:1]
        department_map = {
            "m": "機械工学科",
            "e": "電気電子工学科",
            "d": "電子制御工学科",
            "j": "情報工学科",
            "c": "環境都市工学科",
        }

        department_str = department_map.get(department_id)
        if not department_str:
            print(f"Unknown department ID: {department_id} for student {student_id}")
            return None

        try:
            admission_year = int("20" + student_id[1:3])
        except ValueError:
            print(f"Invalid year format in student ID: {student_id}")
            return None

        return department_str, admission_year

    def _update_single_student(self, student: StudentInfo, school: School) -> bool:
        try:
            if not student.student_id:
                return False

            # 学科と入学年度の解析
            parse_result = self._parse_student_id(student.student_id)
            if not parse_result:
                return False
            department_str, admission_year = parse_result

            # 学科の取得
            department = Department.objects.get(
                school=school,
                name=department_str,
                admission_year=admission_year,
            )
            student.department = department
            student.save()
            return True

        except Exception as e:
            print(f"Error updating student {student.student_id}: {e}")
            return False

    async def process_students(self):
        """学生の基本情報を更新"""

        @sync_to_async
        def update_details():
            school = School.objects.get(name__contains="木更津")
            students = StudentInfo.objects.select_related("user").filter(
                user__role=UserRole.STUDENT
            )

            updated_count = 0
            error_count = 0

            for student in students:
                if self._update_single_student(student, school):
                    updated_count += 1
                else:
                    error_count += 1

            print(f"Students updated: {updated_count}, errors: {error_count}")
            return updated_count, error_count

        return await update_details()

    # ========== 教師関連 ==========
    async def process_teachers(self):
        """教師情報の処理（基本情報 + ManyToMany）"""
        await self.update_teacher_basic_info()
        await self.update_teacher_subjects()

    async def update_teacher_basic_info(self):
        """教師の基本情報を更新"""

        @sync_to_async
        def update_details():
            school = School.objects.get(name__contains="木更津")
            teachers = TeacherInfo.objects.select_related("user").filter(
                user__role=UserRole.TEACHER
            )

            updated_count = 0

            for teacher in teachers:
                try:
                    teacher.subjects.clear()
                    teacher.school = school
                    teacher.save()
                    updated_count += 1
                except Exception as e:
                    print(f"Error updating teacher {teacher.user.email}: {e}")

            print(f"Teachers updated: {updated_count}")
            return updated_count

        return await update_details()

    async def update_teacher_subjects(self):
        """教師の担当教科（ManyToMany）を更新"""

        @sync_to_async
        def update_subjects():
            subject_ctn = 0
            teacher_ctn = 0
            skipped_ctn = 0
            subjects = Subject.objects.all()
            teachers = list(User.objects.filter(role=UserRole.TEACHER))
            choices = [teacher.name for teacher in teachers]
            choice_teacher_map = {teacher.name: teacher for teacher in teachers}

            queries = []
            query_subject_map: Dict[str : List[Subject]] = {}
            for subject in subjects:
                teachers_str = [
                    teacher.strip() for teacher in subject.teachers_str.split(",")
                ]
                for teacher_str in teachers_str:
                    subject_ctn += 1
                    if teacher_str not in query_subject_map:
                        query_subject_map[teacher_str] = [subject]
                    query_subject_map[teacher_str].append(subject)

                    if teacher_str not in queries:
                        queries.append(teacher_str)

            # queries * choices
            score = cdist(queries, choices)
            score = pd.DataFrame(score, index=queries, columns=choices)
            results = score.apply(
                lambda row: row.idxmax() if row.max() >= 75 else None, axis=1
            )
            result = [(query, choice) for query, choice in zip(score.index, results)]

            teachers = []
            for name, user_name in result:
                if subjects and user_name:
                    subjects = query_subject_map[name]
                    user = choice_teacher_map[user_name]
                    teacher = TeacherInfo.objects.get(user=user)
                    teacher.subjects.set(subjects)
                    teacher.save()
                    teacher_ctn += 1
                else:
                    skipped_ctn += 1

            print(
                f"subjects: {subject_ctn}. teacher: {teacher_ctn}. skipped: {skipped_ctn}"
            )

        return await update_subjects()


if __name__ == "__main__":
    import asyncio

    processor = UserProcessor()
    asyncio.run(processor.process_users())
