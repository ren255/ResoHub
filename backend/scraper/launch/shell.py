import asyncio
import argparse

import scraper.settings
from scraper.services import TextFile
import pandas as pd
from IPython.terminal.embed import InteractiveShellEmbed

from scraper.items import *
from scraper.services import *

from content.models import (
    School,
    Department,
    SchoolClass,
    Exam,
    ExamGroupe,
    Subject,
    SubjectGroupe,
)

pd.set_option("display.unicode.east_asian_width", True)


async def load_files(scrape_id):
    global file_school, file_department_overview, file_department_detail, file_subject_catalog, file_subject_detail, file_subject_content
    global df_school, df_department_overview, df_department_detail, df_subject_catalog, df_subject_detail, df_subject_content

    school = TextFile(scrape_id, "school_id", "jsonl")
    file_school = await school.read_file()
    df_school = await school.read_as_dataframe()

    department_overview = TextFile(scrape_id, "department_overview", "jsonl")
    file_department_overview = await department_overview.read_file()
    df_department_overview = await department_overview.read_as_dataframe()

    department_detail = TextFile(scrape_id, "department_id", "jsonl")
    file_department_detail = await department_detail.read_file()
    df_department_detail = await department_detail.read_as_dataframe()

    subject_catalog = TextFile(scrape_id, "subject_id", "jsonl")
    file_subject_catalog = await subject_catalog.read_file()
    df_subject_catalog = await subject_catalog.read_as_dataframe()

    subject_detail = TextFile(scrape_id, "subject_detail", "jsonl")
    file_subject_detail = await subject_detail.read_file()
    df_subject_detail = await subject_detail.read_as_dataframe()

    subject_content = TextFile(scrape_id, "subject_contents", "jsonl")
    file_subject_content = await subject_content.read_file()
    df_subject_content = await subject_content.read_as_dataframe()

    print("vals:")
    for name, val in globals().items():
        print(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run interactive shell with preloaded data"
    )
    parser.add_argument(
        "--scrape-id", type=str, required=True, help="ID of the scrape to export"
    )
    args = parser.parse_args()

    global scrape_id
    scrape_id = args.scrape_id

    # ファイルを非同期で読み込み
    asyncio.run(load_files(scrape_id))

    # 非同期対話シェルを起動
    ipshell = InteractiveShellEmbed()
    ipshell.autoawait = True
    ipshell()
