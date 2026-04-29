from rest_framework import viewsets
from ..models import School, Department, SyllabusDepartment, SchoolClass, GradeClass
from ..serializers import (
    SchoolSerializer,
    DepartmentSerializer,
    SyllabusDepartmentSerializer,
    SchoolClassSerializer,
    GradeClassSerializer,
)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SyllabusDepartmentViewSet(viewsets.ModelViewSet):
    queryset = SyllabusDepartment.objects.all()
    serializer_class = SyllabusDepartmentSerializer


class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer


class GradeClassViewSet(viewsets.ModelViewSet):
    queryset = GradeClass.objects.all()
    serializer_class = GradeClassSerializer
