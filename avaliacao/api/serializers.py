from rest_framework import serializers
from rest_framework.fields import DateTimeField

from avaliacao.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    data_criacao = DateTimeField(format="%d/%m/%Y %H:%M:%S", input_formats=['%d/%m/%Y %H:%M:%S', 'iso-8601'])

    class Meta:
        model = Avaliacao
        fields = '__all__'


