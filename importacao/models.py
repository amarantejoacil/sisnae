from django.db import models
from core.models import Base
from django.contrib.auth.models import User


class Importacao(Base):
    descricao = models.CharField('Descrição', max_length=100)
    arquivo = models.FileField(upload_to='xlsx')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    STATUS_ANEXO = (
        (1, "Arquivo Processado com sucesso"),
        (2, "Arquivo não Processado"),
        (3, "Erro ao realizar processamentos, verifique o padrão do arquivo!"),
    )
    situacao = models.IntegerField('Tipo do Curso', choices=STATUS_ANEXO, default=2)

    def __str__(self):
        return self.descricao
