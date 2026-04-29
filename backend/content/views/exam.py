from rest_framework import viewsets
from ..models import Exam, ExamGroupe
from ..serializers import ExamSerializer, ExamGroupeSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamGroupeViewSet(viewsets.ModelViewSet):
    queryset = ExamGroupe.objects.all()
    serializer_class = ExamGroupeSerializer
