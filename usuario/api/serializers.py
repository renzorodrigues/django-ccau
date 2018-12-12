from rest_framework import serializers
from usuario.models import Atendido, Avaliador, Responsavel


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'
        depth = 1


class ResponsavelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'
        depth = 0


class AtendidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendido
        fields = '__all__'
        depth = 1


class AtendidoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendido
        fields = '__all__'
        depth = 0


class AvaliadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliador
        fields = '__all__'
        depth = 1
