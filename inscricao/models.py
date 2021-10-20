from django.db import models
from core.models import Base
from aluno.models import Aluno
from edital.models import Edital
from questionario.models import Questionario


class Inscricao(Base):
    questionario = models.ForeignKey(Questionario, on_delete=models.PROTECT)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    edital = models.ForeignKey(Edital, on_delete=models.PROTECT)
    SITUACAO_INSCRICAO = (
        (1, 'Inscrição realizada'),
        (2, 'Realizar Correção'),
        (3, 'Inscrição Deferida'),
        (4, 'Inscrição Indeferida'),
        (5, 'Inscrição Cancelada'),
    )
    situacao_obs = models.CharField('Observação da inscrição', max_length=200, null=True, blank=True)
    inscricao_situacao = models.IntegerField(choices=SITUACAO_INSCRICAO, default=1)
    # inscricao_dta_ini_correcao = models.DateTimeField('Data para correção', null=True, blank=True)
    # inscricao_dta_fim_correcao = models.DateTimeField('Data para correção', null=True, blank=True)

    def __str__(self):
        return str(self.aluno)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'


