from urllib.parse import urlparse, parse_qs
from typing import Dict


def url_analyzer(url: str) -> Dict[str, str]:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return {
        "school_id": query_params.get("school_id", [None])[0],
        "department_id": query_params.get("department_id", [None])[0],
        "year": query_params.get("year", [None])[0],
        "subject_code": query_params.get("subject_code", [None])[0],
    }


from enum import Enum
from typing import Optional


class PageType(Enum):
    SCHOOLS = "PublicSchools"
    DEPARTMENTS = "PublicDepartments"
    SUBJECTS = "PublicSubjects"
    SUBJECT_MAPPING = "PublicSubjectMapping"
    CURRICULUM_MAP = "PublicCurriculumMap"
    LEARNING_MAP = "PublicLearningMap"
    SYLLABUS = "PublicSyllabus"


def url_generator(
    page: PageType,
    school_id: Optional[str] = None,
    department_id: Optional[str] = None,
    year: Optional[str] = None,
    subject_code: Optional[str] = None,
    lang: str = "ja",
) -> str:
    base = "https://syllabus.kosen-k.go.jp/Pages"
    params = []

    if page == PageType.SCHOOLS:
        pass
    elif page == PageType.DEPARTMENTS:
        if school_id is None:
            raise ValueError("school_id is required")
        params.append(f"school_id={school_id}")
    elif page in [
        PageType.SUBJECTS,
        PageType.SUBJECT_MAPPING,
        PageType.CURRICULUM_MAP,
        PageType.LEARNING_MAP,
    ]:
        if None in [school_id, department_id, year]:
            raise ValueError("school_id, department_id, year are required")
        params.extend(
            [f"school_id={school_id}", f"department_id={department_id}", f"year={year}"]
        )
    elif page == PageType.SYLLABUS:
        if None in [school_id, department_id, year, subject_code]:
            raise ValueError(
                "school_id, department_id, year, subject_code are required"
            )
        params.extend(
            [
                f"school_id={school_id}",
                f"department_id={department_id}",
                f"subject_code={subject_code}",
                f"year={year}",
            ]
        )

    params.append(f"lang={lang}")
    query = "&".join(params)
    return f"{base}/{page.value}?{query}" if params else f"{base}/{page.value}"
