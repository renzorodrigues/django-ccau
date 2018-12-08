from rest_framework import serializers
from turma.models import Turma


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
        depth = 0


class TurmaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


def get_serializer_class(self):
    method = self.request.method
    if method == 'PUT' or method == 'POST':
        return TurmaWriteSerializer
    else:
        return TurmaSerializer



