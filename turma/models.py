from django.db import models
from unidade.models import Unidade


class Turma(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    PERIODO_CHOICES = (
        ("M", "Manhã"),
        ("T", "Tarde"),
    )
    periodo = models.CharField("Período", max_length=1, null=True, choices=PERIODO_CHOICES)
    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE,
        null=True
    )

    object = models.Manager()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

