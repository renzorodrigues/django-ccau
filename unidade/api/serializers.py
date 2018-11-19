from rest_framework import serializers
from unidade.models import Unidade


class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'
        depth = 2



