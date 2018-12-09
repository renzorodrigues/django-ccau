from django.db import models
from datetime import datetime
from endereco.models import Endereco
from turma.models import Turma


class Usuario(models.Model):
    nome = models.CharField("Nome", max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class Atendido(Usuario):
    SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino")
    )
    matricula = models.CharField("Matrícula", max_length=10, unique=True)
    sexo = models.CharField("Sexo", max_length=2, choices=SEXO)
    data_nascimento = models.DateField("Data de Nascimento")
    data_matricula = models.DateField("Data de Matrícula", blank=True, null=True)
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.CASCADE,
        null=True
    ),
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        null=True
    )
    responsaveis = models.ManyToManyField(
        "Responsavel"
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
    tipo_responsavel = models.CharField("Tipo do Responsável", max_length=2, choices=TIPOS, null=True)

    object = models.Manager()
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Responsável"
        verbose_name_plural = "Responsáveis"
