from django.db import models
from core.models import Pessoa, Base
from curso.models import Curso

from stdimage.models import StdImageField
from django.contrib.auth import get_user_model

class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT, null=True)
    matricula = models.IntegerField('Matricula', unique=True)
    aluno_status = models.BooleanField('Aluno ativo? ', default=True)

    def __str__(self):
        return str(self.matricula)

class Modalidade(Base):
    modalidade_desc = models.CharField('Descricao', max_length=100)
    modalidade_status = models.BooleanField('Modalidade ativa?', default=True)

    def __str__(self):
        return str(self.modalidade_desc)