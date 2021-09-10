from django.db import models
from core.models import Pessoa, Base
from curso.models import Curso, Semestre
from edital.models import Edital
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Aluno(models.Model):
    aluno_status = models.BooleanField('Aluno ativo? ', default=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    semestre = models.ForeignKey(Semestre, on_delete=models.RESTRICT)
    aluno_matricula = models.BigIntegerField('Matricula', unique=True)
    IncPor = models.IntegerField('Incluido Por', null=True, blank=True)
    AltPor = models.IntegerField('Alterado Por', null=True, blank=True)
    IncEm = models.DateTimeField('Incluido Em', auto_now_add=True)
    AltEm = models.DateTimeField('Alterado Em', auto_now=True)


    def __str__(self):
        return str(self.aluno_matricula)

