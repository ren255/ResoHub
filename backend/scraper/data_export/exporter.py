import scraper.settings
from content.models import (
    School,
    Department,
    SchoolClass,
    Exam,
    ExamGroupe,
    Subject,
    SubjectGroupe,
)
from scraper.services import TextFile
import json
from asgiref.sync import sync_to_async
import itertools


class Exporter:
    def __init__(self, scrape_id):
        self.scrape_id = scrape_id

    async def get(self):
        self.school = TextFile(self.scrape_id, "school_id", "jsonl")
        self.file_school = await self.school.read_file()
        self.df_school = await self.school.read_as_dataframe()
        self.department_overview = TextFile(
            self.scrape_id, "department_overview", "jsonl"
        )
        self.file_department_overview = await self.department_overview.read_file()
        self.df_department_overview = await self.department_overview.read_as_dataframe()

        self.department_detail = TextFile(self.scrape_id, "department_id", "jsonl")
        self.file_department_detail = await self.department_detail.read_file()
        self.df_department_detail = await self.department_detail.read_as_dataframe()

        self.subject_catalog = TextFile(self.scrape_id, "subject_id", "jsonl")
        self.file_subject_catalog = await self.subject_catalog.read_file()
        self.df_subject_catalog = await self.subject_catalog.read_as_dataframe()

        self.subject_detail = TextFile(self.scrape_id, "subject_detail", "jsonl")
        self.file_subject_detail = await self.subject_detail.read_file()
        self.df_subject_detail = await self.subject_detail.read_as_dataframe()

        self.subject_content = TextFile(self.scrape_id, "subject_contents", "jsonl")
        self.file_subject_content = await self.subject_content.read_file()
        self.df_subject_content = await self.subject_content.read_as_dataframe()

    async def run(self):
        print("start")
        await self.get()
        print("got")
        await self.delete()
        print("deleted")
        await self.process_org()
        await self.process_class()
        await self.process_exam()
        await self.process_subject()
        print("end")

    async def delete(self):
        @sync_to_async
        def delete_all():
            School.objects.all().delete()
            Department.objects.all().delete()
            SchoolClass.objects.all().delete()
            Exam.objects.all().delete()
            ExamGroupe.objects.all().delete()
            Subject.objects.all().delete()
            SubjectGroupe.objects.all().delete()

        await delete_all()

    async def process_org(self):
        @sync_to_async
        def create_schools():
            objects = []
            for school in self.file_school.split("\n"):
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
            for department, department_detail in zip(
                self.file_department_detail.split("\n"),
                self.file_department_detail.split("\n"),
            ):
                if not department.strip() and not department_detail.strip():
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

            departments_list = self.df_subject_detail["department_id"].unique()
            for department_id in departments_list:
                grades = self.df_subject_detail[
                    self.df_subject_detail["department_id"] == department_id
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


import argparse
import asyncio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run data exporter")
    parser.add_argument(
        "--scrape-id", type=str, required=True, help="ID of the scrape to export"
    )
    args = parser.parse_args()

    exporter = Exporter(scrape_id=args.scrape_id)
    asyncio.run(exporter.run())
