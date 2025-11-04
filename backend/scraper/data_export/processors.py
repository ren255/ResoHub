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


class Processor:
    def __init__(self, file_data: FileData, df_data: DataFrameData):
        self.file = file_data
        self.df = df_data

    async def process(self):
        await self.process_org()
        await self.process_class()
        await self.process_subject()
        await self.process_exam()

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
                grades = self.df.subject_detail[
                    self.df.subject_detail["department_id"] == department_id
                ]["grade"].unique()

                # TODO remove
                import re

                grades = [re.sub(r"\D", "", grade) for grade in grades]

                departments = Department.objects.filter(code=department_id)

                for grade, department in itertools.product(grades, departments):
                    obj = SchoolClass(department=department, grade=grade)
                    objects.append(obj)

            SchoolClass.objects.bulk_create(objects)

        await create_classes()

    async def process_exam(self):
        pass

    async def process_subject(self):
        pass
