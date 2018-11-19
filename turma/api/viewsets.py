from rest_framework import viewsets
from turma.models import Turma
from .serializers import TurmaSerializer


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.object.all()
    serializer_class = TurmaSerializer
