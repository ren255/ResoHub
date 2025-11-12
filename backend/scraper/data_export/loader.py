from dataclasses import dataclass
from typing import Tuple
import pandas as pd
from scraper.services import TextFile


@dataclass
class FileData:
    """Raw file content"""

    school: str
    department_overview: str
    department_detail: str
    subject_catalog: str
    subject_detail: str
    subject_content: str


@dataclass
class DataFrameData:
    """Parsed DataFrame content"""

    school: pd.DataFrame
    department_overview: pd.DataFrame
    department_detail: pd.DataFrame
    subject_catalog: pd.DataFrame
    subject_detail: pd.DataFrame
    subject_content: pd.DataFrame


class DataLoader:
    """Loads and parses all scrape data files"""

    def __init__(self, scrape_id: str):
        self.scrape_id = scrape_id

    async def load(self) -> Tuple[FileData, DataFrameData]:
        """Load all data files and return structured data"""

        # Initialize TextFile instances
        school = TextFile(self.scrape_id, "school_id", "jsonl")
        department_overview = TextFile(self.scrape_id, "department_overview", "jsonl")
        department_detail = TextFile(self.scrape_id, "department_id", "jsonl")
        subject_catalog = TextFile(self.scrape_id, "subject_id", "jsonl")
        subject_detail = TextFile(self.scrape_id, "subject_detail", "jsonl")
        subject_content = TextFile(self.scrape_id, "subject_contents", "jsonl")

        # Load raw files
        files = FileData(
            school=await school.read_file(),
            department_overview=await department_overview.read_file(),
            department_detail=await department_detail.read_file(),
            subject_catalog=await subject_catalog.read_file(),
            subject_detail=await subject_detail.read_file(),
            subject_content=await subject_content.read_file(),
        )

        # Load DataFrames
        dataframes = DataFrameData(
            school=await school.read_as_dataframe(),
            department_overview=await department_overview.read_as_dataframe(),
            department_detail=await department_detail.read_as_dataframe(),
            subject_catalog=await subject_catalog.read_as_dataframe(),
            subject_detail=await subject_detail.read_as_dataframe(),
            subject_content=await subject_content.read_as_dataframe(),
        )

        return (files, dataframes)
