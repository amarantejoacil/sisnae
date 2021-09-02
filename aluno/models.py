from django.db import models
from core.models import Pessoa, Base
from curso.models import Curso

from stdimage.models import StdImageField
from django.contrib.auth import get_user_model

class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, null=True)
    aluno_matricula = models.IntegerField('Matricula', unique=True)
    aluno_status = models.BooleanField('Aluno ativo? ', default=True)
    FORMA_INGRESSO_CHOICES = (
        ('A', "Por Ampla Concorrência"),
        ('C', "Por Meio de Cota"),
    )
    aluno_form_ingre = models.CharField('Sexo', choices=FORMA_INGRESSO_CHOICES, max_length=1)
    aluno_possui_conta = models.BooleanField('Possui conta?', default=True)
    aluno_agencia = models.CharField('N° da Agência',max_length=20)
    aluno_conta = models.CharField('N° da Conta', max_length=20)

    TIPO_CONTA_CHOICES = (
        ('CP', "Conta Poupança"),
        ('CC', "Conta Corrente"),
        ('PP', "Conta Poupex"),
        ('PO', "Conta Poupança Ouro"),
        ('CU', "Conta Universitária"),
        ('CL', "Conta Salário"),
    )

    aluno_tipo_conta = models.CharField('Tipo de conta', choices=TIPO_CONTA_CHOICES, max_length=2)
    aluno_nome_pai = models.CharField('Nome do Pai', max_length=100, null=True, blank=True)
    aluno_nome_mae = models.CharField('Nome da Mãe', max_length=100)

    ESCOLARIDADE_CHOICES = (
        (1, "Ensino Fundamental Incompleto"),
        (2, "Ensino Fundamental Completo"),
        (3, "Ensino Médio Incompleto"),
        (4, "Ensino Médio Completo"),
        (5, "Ensino Superior Incompleto"),
        (6, "Ensino Superior Completo"),
        (7, "Pós-Graduação"),
        (8, "Mestrado"),
        (9, "Doutorado"),
    )

    aluno_esc_pai = models.IntegerField('Escolaridade do Pai', choices=ESCOLARIDADE_CHOICES, max_length=1)
    aluno_esc_mae = models.IntegerField('Escolaridade da Mãe', choices=ESCOLARIDADE_CHOICES, max_length=1)

    def __str__(self):
        return str(self.aluno_matricula)

class Modalidade(Base):
    modalidade_desc = models.CharField('Descricao', max_length=100)
    modalidade_status = models.BooleanField('Modalidade ativa?', default=True)

    def __str__(self):
        return str(self.modalidade_desc)