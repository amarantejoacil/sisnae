from core.models import Base
from django.db import models


class Edital(Base):
    descricao = models.CharField('Descrição', max_length=100)
    numero = models.PositiveIntegerField('Nº do Edital')
    ano = models.PositiveIntegerField('Informe o ano do Edital')
    data_hora_inicio = models.DateTimeField('Validade Data/Hora Inicio:', null=True)
    data_hora_fim = models.DateTimeField('Validade Data/Hora Inicio:', null=True)
    edital_status = models.BooleanField('Edital ativo?', default=True)

    class Meta:
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'

    def __str__(self):
        return self.descricao


class PublicacaoEdital(Base):
    edital = models.ForeignKey("Edital", on_delete=models.CASCADE)
    publicacao_descricao = models.CharField('Descrição', max_length=150)
    publicacao_anexo_arq = models.CharField(max_length=100)
    publicacao_data = models.DateField('Data da publicação', null=True, blank=True)

    def __str__(self):
        return self.publicacao_descricao

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
