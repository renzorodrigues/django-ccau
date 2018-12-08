from django.db import models
from turma.models import Turma


class Unidade(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    turmas = models.ManyToManyField(
        Turma
    )

    object = models.Manager()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
