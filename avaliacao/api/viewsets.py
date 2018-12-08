from rest_framework import viewsets
from avaliacao.models import Avaliacao
from avaliacao.api.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.object.all()
    serializer_class = AvaliacaoSerializer
