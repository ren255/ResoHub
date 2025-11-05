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
import itertools
import json
import re


class Processor:
    def __init__(self, file_data: FileData, df_data: DataFrameData):
        self.file = file_data
        self.df = df_data

    async def process(self):
        await self.process_org()
        print("org done")
        await self.process_class()
        print("class done")
        await self.process_subject()
        print("subject done")
        await self.process_exam()
        print("subject done")

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

    async def process_exam(self):
        pass

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
                    teachers=data["teachers"],
                    textbooks=data["textbooks"],
                    school_class=school_class,
                )
                objects.append(obj)
            Subject.objects.bulk_create(objects)

        await create_subjects()
