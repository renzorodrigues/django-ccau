from rest_framework import serializers
from rest_framework.fields import DateField
from usuario.models import Atendido, Avaliador, Responsavel
from endereco.api.serializers import EnderecoSerializer


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = '__all__'


class AtendidoSerializer(serializers.ModelSerializer):

    responsaveis = ResponsavelSerializer(many=True)
    data_nascimento = DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    data_matricula = DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])
    endereco = EnderecoSerializer()

    class Meta:
        model = Atendido
        fields = '__all__'


class AvaliadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliador
        fields = '__all__'


