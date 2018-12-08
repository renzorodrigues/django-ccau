from rest_framework import serializers
from rest_framework.fields import DateField
from usuario.models import Atendido, Avaliador, Responsavel


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'
        depth = 1


class AtendidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendido
        fields = '__all__'
        depth = 0


class AtendidoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendido
        fields = '__all__'


def get_serializer_class(self):
    method = self.request.method
    if method == 'PUT' or method == 'POST':
        return AtendidoWriteSerializer
    else:
        return AtendidoSerializer


class AvaliadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliador
        fields = '__all__'
        depth = 1


