from django.db import models
from core.models import Base
from django.contrib.auth.models import User


class Importacao(Base):
    descricao = models.CharField('Descrição', max_length=100)
    arquivo = models.FileField(upload_to='xlsx')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
