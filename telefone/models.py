from django.db import models
from usuario.models import Atendido


class Telefone(models.Model):
    ddd = models.CharField("DDD", max_length=2)
    numero = models.CharField("Número", max_length=10)
    atendido = models.ForeignKey(Atendido, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.numero
    
    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"
