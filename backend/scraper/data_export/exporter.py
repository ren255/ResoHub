from content.models import (
    School,
    Department,
    SchoolClass,
    User,
    Exam,
    ExamGroupe,
    Subject,
    SubjectGroupe,
)
from scraper.services import TextFile
import json


class Exporter:
    def __init__(self, scrape_id):
        self.scrape_id = scrape_id

    async def get(self):
        self.file_school = await TextFile(
            self.scrape_id, "school_id", "jsonl"
        ).read_file()
        self.file_department_overview = await TextFile(
            self.scrape_id, "department_overview", "jsonl"
        ).read_file()
        self.file_department_detail = await TextFile(
            self.scrape_id, "department_id", "jsonl"
        ).read_file()
        self.file_subject_catalog = await TextFile(
            self.scrape_id, "subject_id", "jsonl"
        ).read_file()
        self.file_subject_detail = await TextFile(
            self.scrape_id, "subject_detail", "jsonl"
        ).read_file()
        self.file_subject_content = await TextFile(
            self.scrape_id, "subject_contents", "jsonl"
        ).read_file()

    async def run(self):
        await self.get()
        self.process_school(self.file_school)
        self.process_department()
        self.process_exam()
        self.process_subject()

    async def process_school(self):
        schools = []
        for school in self.file_school.split("\n"):
            data = json.loads(school)
            obj = School.objects.create()
        School.objects.bulk_create()

    async def process_department(self):
        pass

    async def process_exam(self):
        pass

    async def process_subject(self):
        pass
