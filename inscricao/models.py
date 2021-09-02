from django.db import models
from core.models import Base

class Inscricao(Base):
    situacao_obs = models.CharField('Observação da inscrição', max_length=200, null=True)


class Situacao(Base):
    descricao = models.CharField('Descrição', max_length=150)
    situacao_status = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'


class Modalidade(Base):
    modalidade_desc = models.CharField('Descricao', max_length=100)
    modalidade_status = models.BooleanField('Modalidade ativa?', default=True)

    def __str__(self):
        return str(self.modalidade_desc)