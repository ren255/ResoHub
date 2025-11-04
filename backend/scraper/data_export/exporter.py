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


class Exporter:
    def __init__(self, scrape_id):
        self.scrape_id = scrape_id

        self.file_school = TextFile(self.scrape_id, "school_id", "jsonl")
        self.file_department_overview = TextFile(
            self.scrape_id, "department_overview", "jsonl"
        )
        self.file_department_detail = TextFile(self.scrape_id, "department_id", "jsonl")
        self.file_subject_catalog = TextFile(self.scrape_id, "subject_id", "jsonl")
        self.file_subject_detail = TextFile(self.scrape_id, "subject_detail", "jsonl")
        self.file_subject_content = TextFile(
            self.scrape_id, "subject_contents", "jsonl"
        )

    def run(self):
        self.process_school()
        self.process_department()
        self.process_exam()
        self.process_subject()
