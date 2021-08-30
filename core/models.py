from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model


class Base(models.Model):
    IncPor = models.IntegerField('Incluido Por', null=True, blank=True)
    AltPor = models.IntegerField('Alterado Por', null=True, blank=True)
    IncEm = models.DateTimeField('Incluido Em', auto_now_add=True)
    AltEm = models.DateTimeField('Alterado Em', auto_now=True)

    class Meta:
        abstract = True


class Pessoa(Base):
    nome = models.CharField('Nome', max_length=150)


class Aluno(Pessoa):
    matricula = models.IntegerField('Matricula', unique=True)


"""
class Banco(Base):
    banco_id = models.IntegerField(primary_key=True)
    descricao = models.CharField('Descrição', max_length=100)
"""