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
    responsaveis_pk = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Atendido
        fields = '__all__'
        depth = 0


class AvaliadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliador
        fields = '__all__'
        depth = 1
