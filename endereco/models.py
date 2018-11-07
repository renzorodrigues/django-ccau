from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField("Logradouro", max_length=200)
    numero = models.CharField("Número", max_length=10)
    bairro = models.CharField("Bairro", max_length=50)
    cep = models.CharField("CEP", max_length=9, blank=True)
    cidade = models.CharField("Cidade", max_length=50)

    object = models.Manager()

    def __str__(self):
        return self.logradouro

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"