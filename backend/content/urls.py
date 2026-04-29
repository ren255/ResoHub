from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
from .views.organization import (
    SchoolViewSet,
    DepartmentViewSet,
    SyllabusDepartmentViewSet,
    SchoolClassViewSet,
    GradeClassViewSet,
)
from .views.subject import SubjectViewSet, SubjectGroupeViewSet
from .views.exam import ExamViewSet, ExamGroupeViewSet
from .views.user_info import StudentInfoViewSet, TeacherInfoViewSet, UserSettingViewSet

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"school", SchoolViewSet, basename="school")
router.register(r"department", DepartmentViewSet, basename="department")
router.register(
    r"syllabus-department", SyllabusDepartmentViewSet, basename="syllabus-department"
)
router.register(r"school-class", SchoolClassViewSet, basename="school-class")
router.register(r"grade-class", GradeClassViewSet, basename="grade-class")
router.register(r"subject", SubjectViewSet, basename="subject")
router.register(r"subject-groupe", SubjectGroupeViewSet, basename="subject-groupe")
router.register(r"exam", ExamViewSet, basename="exam")
router.register(r"exam-groupe", ExamGroupeViewSet, basename="exam-groupe")
router.register(r"student-info", StudentInfoViewSet, basename="student-info")
router.register(r"teacher-info", TeacherInfoViewSet, basename="teacher-info")
router.register(r"user-setting", UserSettingViewSet, basename="user-setting")

urlpatterns = router.urls
