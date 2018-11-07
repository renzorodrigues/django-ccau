from django.db import models


class Unidade(models.Model):
    TIPOS_UNIDADES = (
        ("CN", "CANAÃ"),
        ("SP", "SHOPPING PARK"),
        ("JG", "JARAGUÁ"),
        ("PN", "PLANALTO"),
        ("PQ", "PEQUIS"),
    )
    unidade = models.CharField("Unidade", max_length=2, choices=TIPOS_UNIDADES)
    descricao = models.CharField("Descrição", max_length=100)

    object = models.Manager()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
