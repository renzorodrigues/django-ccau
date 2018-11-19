from rest_framework import serializers
from rest_framework.fields import DateTimeField

from avaliacao.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        depth = 1


