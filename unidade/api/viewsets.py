from rest_framework import viewsets
from unidade.models import Unidade
from .serializers import UnidadeSerializer


class UnidadeViewSet(viewsets.ModelViewSet):
    serializer_class = UnidadeSerializer
    queryset = Unidade.object.all()
