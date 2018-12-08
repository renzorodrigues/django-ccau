from rest_framework import serializers
from avaliacao.models import Avaliacao
from usuario.api.serializers import AtendidoSerializer, AvaliadorSerializer


class AvaliacaoSerializer(serializers.ModelSerializer):

    atendido = AtendidoSerializer()
    avaliador = AvaliadorSerializer()

    class Meta:
        model = Avaliacao
        fields = ('id','demanda','queixa','descricao','atendido','avaliador')


