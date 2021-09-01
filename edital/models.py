from core.models import Base
from django.db import models

class Edital(Base):
    descricao = models.CharField('Descrição', max_length=100)
    numero = models.PositiveIntegerField('Nº do Edital')
    ano = models.PositiveIntegerField('Informe o ano do Edital')
    data_inicio = models.DateTimeField('Validade Data/Hora Inicio:', null=True)
    data_fim = models.DateTimeField('Validade Data/Hora Inicio:', null=True)

    def __str__(self):
        return self.descricao
