from django.db import models
from core.models import Base
from aluno.models import Aluno
from edital.models import Edital



class Inscricao(Base):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    modalidade = models.ForeignKey("Modalidade", on_delete=models.CASCADE)

    SITUACAO_INSCRICAO = (
        (1, 'inscrição realizada'),
        (2, 'realizar correção'),
        (3, 'inscrição deferida'),
        (4, 'inscrição indeferida'),
    )
    inscricao_situacao = models.IntegerField(choices=SITUACAO_INSCRICAO, default=1)

    situacao_obs = models.CharField('Observação da inscrição', max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.aluno)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

"""
class Situacao(Base):
    descricao = models.CharField('Descrição', max_length=150)
    #situacao_status = models.BooleanField('Ativo?', default=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'
"""


class Modalidade(Base):
    modalidade_desc = models.CharField('Descricao', max_length=100)
    modalidade_status = models.BooleanField('Modalidade ativa?', default=True)

    def __str__(self):
        return self.modalidade_desc
