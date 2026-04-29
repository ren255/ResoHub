from rest_framework import viewsets
from ..models import StudentInfo, TeacherInfo, UserSetting
from ..serializers import (
    StudentInfoSerializer,
    TeacherInfoSerializer,
    UserSettingSerializer,
)


class StudentInfoViewSet(viewsets.ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer


class TeacherInfoViewSet(viewsets.ModelViewSet):
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherInfoSerializer


class UserSettingViewSet(viewsets.ModelViewSet):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingSerializer
