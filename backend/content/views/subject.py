from rest_framework import viewsets
from ..models import Subject, SubjectGroupe
from ..serializers import SubjectSerializer, SubjectGroupeSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectGroupeViewSet(viewsets.ModelViewSet):
    queryset = SubjectGroupe.objects.all()
    serializer_class = SubjectGroupeSerializer
