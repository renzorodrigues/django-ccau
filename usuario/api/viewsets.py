from rest_framework import viewsets
from usuario.models import Atendido, Avaliador, Responsavel
from .serializers import AtendidoSerializer, AvaliadorSerializer, ResponsavelSerializer, AtendidoWriteSerializer, \
    ResponsavelWriteSerializer


class AtendidoViewSet(viewsets.ModelViewSet):
    queryset = Atendido.object.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return AtendidoWriteSerializer
        else:
            return AtendidoSerializer


class AvaliadorViewSet(viewsets.ModelViewSet):
    queryset = Avaliador.object.all()
    serializer_class = AvaliadorSerializer


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.object.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ResponsavelWriteSerializer
        else:
            return ResponsavelSerializer
