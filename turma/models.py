from django.db import models


class Turma(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    PERIODO_CHOICES = (
        ("M", "Manhã"),
        ("T", "Tarde"),
        ("I", "Integral")
    )
    periodo = models.CharField("Período", max_length=1, null=True, choices=PERIODO_CHOICES)

    object = models.Manager()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

