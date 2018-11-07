from django.db import models
from django.utils import timezone

from endereco.models import Endereco


class Usuario(models.Model):
    nome = models.CharField("Nome", max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Atendido(Usuario):
    matricula = models.CharField("Matrícula", max_length=10, unique=True)
    data_nascimento = models.DateField("Data de Nascimento")
    data_matricula = models.DateField("Data de Matrícula", blank=True, null=True)
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.CASCADE,
        null=True
    )
    responsaveis = models.ManyToManyField(
        "Responsavel",
        verbose_name="Responsáveis"
    )

    object = models.Manager()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Atendido"
        verbose_name_plural = "Atendidos"


class Avaliador(Usuario):
    cargo = models.CharField("Cargo", max_length=50)

    object = models.Manager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Avaliador"
        verbose_name_plural = "Avaliadores"


class Responsavel(Usuario):
    TIPOS = (
        ("PA", "Pai"),
        ("MA", "Mãe"),
        ("RL", "Responsável Legal"),
    )
    tipo = models.CharField("Tipos Responsável", max_length=2, choices=TIPOS)

    object = models.Manager()
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsáveis"
