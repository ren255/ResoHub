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
from asgiref.sync import sync_to_async
from .loader import DataLoader
from .processors import Processor

import time


class Exporter:
    def __init__(self, scrape_id):
        self.scrape_id = scrape_id

    async def run(self):
        loader = DataLoader(self.scrape_id)
        await self.delete()
        files, dfs = await loader.load()
        processor = Processor(files, dfs)
        # await processor.process()

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
