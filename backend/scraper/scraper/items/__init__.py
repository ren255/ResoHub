# https://docs.scrapy.org/en/latest/topics/items.html

from .colleges_overview import CollegesOverviewItem
from .departments_overview import DepartmentsOverviewItem
from .department_detail import DepartmentDetailItem
from .subject_catalog import SubjectCatalogItem
from .subject_detail import SubjectDetailItem, SubjectContentItem


__all__ = [
    "CollegesOverviewItem",
    "DepartmentsOverviewItem",
    "DepartmentDetailItem",
    "SubjectCatalogItem",
    "SubjectDetailItem",
    "SubjectContentItem",
]
