from rest_framework import viewsets
from ..models import Subject, SubjectGroupe
from ..serializers import (
    SubjectSerializer,
    SubjectGroupeSerializer,
    SubjectGroupeListSerializer,
    SubjectGroupeDetailSerializer,
)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectGroupeViewSet(viewsets.ModelViewSet):
    queryset = SubjectGroupe.objects.all()
    serializer_class = SubjectGroupeSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return SubjectGroupeListSerializer
        elif self.action == "retrieve":
            return SubjectGroupeDetailSerializer
        return SubjectGroupeSerializer
