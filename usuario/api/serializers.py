from rest_framework import serializers
from rest_framework.fields import DateField
from usuario.models import Atendido, Avaliador, Responsavel


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'
        depth = 1


class AtendidoSerializer(serializers.ModelSerializer):

    data_nascimento = DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    data_matricula = DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])

    class Meta:
        model = Atendido
        fields = '__all__'
        depth = 2


class AvaliadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliador
        fields = '__all__'
        depth = 1


