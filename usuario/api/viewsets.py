from rest_framework import viewsets
from usuario.models import Atendido, Avaliador, Responsavel
from .serializers import AtendidoSerializer, AvaliadorSerializer, ResponsavelSerializer


class AtendidoViewSet(viewsets.ModelViewSet):
    queryset = Atendido.object.all()
    serializer_class = AtendidoSerializer


class AvaliadorViewSet(viewsets.ModelViewSet):
    queryset = Avaliador.object.all()
    serializer_class = AvaliadorSerializer


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.object.all()
    serializer_class = ResponsavelSerializer
