from content.models import (
    School,
    Department,
    SchoolClass,
    Exam,
    ExamGroupe,
    Subject,
    SubjectGroupe,
)

from .loader import DataFrameData, FileData
from asgiref.sync import sync_to_async
import json
import re


class Processor:
    def __init__(self, file_data: FileData, df_data: DataFrameData):
        self.file = file_data
        self.df = df_data

    async def process(self):
        print("processing...")
        # await sync_to_async(School.objects.all().delete)()
        # await sync_to_async(Department.objects.all().delete)()
        # await self.process_org()
        # print("org done. class...")

        # await sync_to_async(SchoolClass.objects.all().delete)()
        # await self.process_class()
        # print("class done. subject...")

        # await sync_to_async(Subject.objects.all().delete)()
        # await self.process_subject()
        # print("subject done. exam...")

        await sync_to_async(Exam.objects.all().delete)()
        await self.process_exam()
        print("exam done")

        await sync_to_async(ExamGroupe.objects.all().delete)()
        await sync_to_async(SubjectGroupe.objects.all().delete)()

    async def process_org(self):
        @sync_to_async
        def create_schools():
            objects = []
            for school in self.file.school.split("\n"):
                if not school.strip():
                    continue
                data = json.loads(school)
                obj = School(
                    name=data["name"], code=data["school_id"], url=data["url_source"]
                )
                objects.append(obj)
            School.objects.bulk_create(objects)

        await create_schools()

        @sync_to_async
        def create_departments():
            objects = []
            for department in self.file.department_detail.split("\n"):
                if not department.strip():
                    continue
                data = json.loads(department)
                school = School.objects.get(code=data["school_id"])
                obj = Department(
                    school=school,
                    name=data["name"],
                    admission_year=data["admission_year"],
                    url=data["url_source"],
                    code=data["department_id"],
                )
                objects.append(obj)
            Department.objects.bulk_create(objects)

        await create_departments()

    async def process_class(self):
        @sync_to_async
        def create_classes():
            objects = []

            departments_list = self.df.subject_detail["department_id"].unique()
            for department_id in departments_list:
                df_sub_dep = self.df.subject_detail[
                    self.df.subject_detail["department_id"] == department_id
                ]
                grade_mapping: dict = df_sub_dep.set_index("fixed_grade")[
                    "grade_str"
                ].to_dict()

                for fixed_grade, grade_str in grade_mapping.items():
                    departments = Department.objects.filter(code=department_id)
                    for department in departments:
                        year = int(
                            self.df.subject_detail[
                                (
                                    self.df.subject_detail["admission_year"]
                                    == department.admission_year
                                )
                                & (self.df.subject_detail["fixed_grade"] == fixed_grade)
                            ].iloc[0]["year"]
                        )
                        obj = SchoolClass(
                            department=department,
                            grade_str=grade_str,
                            grade=fixed_grade,
                            year=year,
                        )
                        objects.append(obj)

            SchoolClass.objects.bulk_create(objects)

        await create_classes()

    async def process_subject(self):
        @sync_to_async
        def create_subjects():
            objects = []
            for subject in self.file.subject_detail.split("\n"):
                data = json.loads(subject)
                school = School.objects.get(code=data["school_id"])
                department = Department.objects.get(
                    school=school,
                    code=data["department_id"],
                    admission_year=data["admission_year"],
                )
                school_class = SchoolClass.objects.get(
                    department=department,
                    grade_str=data["grade_str"],
                )

                obj = Subject(
                    name=data["subject_name"],
                    code=data["subject_code"],
                    subject_type=data["subject_type"],
                    url=data["url_source"],
                    credits=data["credits"],
                    teachers_str=data["teachers"],
                    textbooks=data["textbooks"],
                    school_class=school_class,
                )
                objects.append(obj)
            Subject.objects.bulk_create(objects)

        await create_subjects()

    async def process_exam(self):
        @sync_to_async
        def create_exams():
            objects = []

            # TODO regex fix
            # 正規の試験名（中間試験、期末試験など）のみを抽出し、
            # 試験の復習・日程・実験名などを除外する
            pattern = r"^(・)?([前後]期\s*)?(中間|定期|期末|学年末|\(期末\))?試験(\(実技テスト\))?(\s*・選択スポーツ)?$"
            # ^                      : 行の先頭
            # (・)?                  : 「・」で始まる場合
            # ([前後]期\s*)?         : 「前期」「後期」とそれに続く空白（省略可）
            # (中間|定期|期末|学年末|\(期末\))? : 試験の種類（省略可、「試験」のみもマッチ）
            #                          ※ \(期末\) は「前期定期(期末)試験」のような特殊ケース
            # 試験                    : 必須の「試験」という文字列
            # (\(実技テスト\))?      : 「(実技テスト)」が付く場合あり
            # (\s*・選択スポーツ)?   : 「・選択スポーツ」が付く特殊ケースあり
            # $                      : 行の末尾

            # TODO 中途dfへid キャッシュ を入れて検索を省略したい
            exam_df = self.df.subject_content[
                self.df.subject_content["content"]
                .str.strip()
                .str.match(pattern, na=False)
            ]
            for row in exam_df.itertuples():
                # subject detailでurlが同じ最初のものを特定
                subject_detail_row = self.df.subject_detail[
                    self.df.subject_detail["url_source"] == row.url_source
                ].iloc[0]
                school = School.objects.get(code=subject_detail_row["school_id"])
                department = Department.objects.get(
                    school=school,
                    code=subject_detail_row["department_id"],
                    admission_year=subject_detail_row["admission_year"],
                )

                school_class = SchoolClass.objects.get(
                    department=department, grade_str=subject_detail_row["grade_str"]
                )
                try:
                    subject = Subject.objects.get(
                        school_class=school_class,
                        name=subject_detail_row["subject_name"],
                        code=subject_detail_row["subject_code"],
                    )
                except:
                    subjects = Subject.objects.filter(
                        school_class=school_class,
                        name=subject_detail_row["subject_name"],
                    )
                    print(
                        f"school_class: admisstion year {school_class.department.admission_year}, {school_class.department.name}"
                    )
                    for subject in subjects:
                        print(f"name : {subject.name} code: {subject.code}")
                    raise KeyboardInterrupt

                obj = Exam(
                    subject=subject,
                    url=row.url_source,
                    quarter=row.quarter,
                    week=row.week,
                    content=row.content,
                    goal=row.goal,
                )
                objects.append(obj)
            Exam.objects.bulk_create(objects)

        await create_exams()
