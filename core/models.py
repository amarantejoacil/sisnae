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
    cidade = models.ForeignKey("Cidade", on_delete=models.RESTRICT, null=True)
    banco = models.ForeignKey("Banco", on_delete=models.RESTRICT, null= True)
    nome = models.CharField('Nome', max_length=150)
    data_nascimento = models.DateField('Data de nascimento', null=True)
    pessoa_status = models.BooleanField('Pessoa ativa?', default=True)

    def __str__(self):
        return self.nome




class Cidade(Base):
    descricao = models.CharField('Descrição', max_length=100)
    cidade_status = models.BooleanField('Cidade ativa?', default=True)

    def __str__(self):
        return self.descricao


class Banco(Base):
    descricao = models.CharField('Descrição', max_length=100)
    banco_status = models.BooleanField('Banco ativo?', default=True)

    def __str__(self):
        return self.descricao
