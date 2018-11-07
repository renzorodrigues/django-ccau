from rest_framework import viewsets
from avaliacao.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.object.all()
