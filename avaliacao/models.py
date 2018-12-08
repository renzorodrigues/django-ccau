from django.db import models
from django.utils import timezone
from usuario.models import Avaliador

from usuario.models import Atendido


class Avaliacao(models.Model):
    TIPOS_DEMANDA = (
        ("IT", "Instituição"),
        ("FM", "Família"),
        ("PR", "Próprio"),
    )
    demanda = models.CharField("Demanda", max_length=2, choices=TIPOS_DEMANDA)
    queixa = models.CharField("Queixa", max_length=100)
    descricao = models.TextField("Descrição")
    data_criacao = models.DateTimeField("Data de Criação", auto_now=timezone.now())
    atendido = models.ForeignKey(
        Atendido,
        on_delete=models.CASCADE
    )
    avaliador = models.ForeignKey(
        Avaliador,
        on_delete=models.CASCADE,
        null=True
    )
    
    object = models.Manager()
    
    def __str__(self):
        return self.queixa
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
