from django.db import models
from core.models import Base
from aluno.models import Aluno
from edital.models import Edital


class Questionario(Base):
    questionario_ano = models.IntegerField('Ano do questionário:')

    SEMESTRE_CHOICES = (
        (1, "1° Semestre"),
        (2, "2° Semestre"),
    )
    questionario_semestre = models.IntegerField('Semestre', choices=SEMESTRE_CHOICES)

    QUEST_FORMA_INGRESSO = (
        ('A', "Por Ampla Concorrência"),
        ('C', "Por Meio de Cota"),
    )
    quest_aluno_form_ingre = models.CharField('Forma de Ingresso',
                                              choices=QUEST_FORMA_INGRESSO,max_length=1)

    QUEST_DISTANCIA_RESIDENCIA = (
        (1, "Aproximadamente 1km"),
        (2, "Aproximadamente 2.5km"),
        (3, "Aproximadamente 5km"),
        (4, "Aproximadamente 7.5km"),
        (5, "Aproximadamente 10km"),
        (6, "Aproximadamente 12.5km"),
        (7, "Aproximadamente 15km"),
        (8, "Aproximadamente 17.5km"),
        (9, "Aproximadamente 20km"),
        (10, "Aproximadamente 30km"),
        (11, "Acima de 30km"),
    )
    quest_aluno_dist_escola = models.IntegerField('Distância aproximada da residência ao Campus em KM?',
                                            choices=QUEST_DISTANCIA_RESIDENCIA)

    QUEST_TRANSPORTE_CAMPUS = (
        (1, "Transporte Coletivo"),
        (2, "Van"),
        (3, "Carro"),
        (4, "Moto"),
        (5, "A pé"),
        (6, "Carona"),
        (7, "Bicicleta"),
    )

    quest_aluno_transporte = models.IntegerField('Informe o meio de transporte '
                                           'utilizado para chegar ao Campus?', choices=QUEST_TRANSPORTE_CAMPUS)

    QUEST_TEMPO_CAMPUS = (
        (1, "Aproximadamente 5 minutos"),
        (2, "Aproximadamente 10 minutos"),
        (3, "Aproximadamente 15 minutos"),
        (4, "Aproximadamente 20 minutos"),
        (5, "Aproximadamente 25 minutos"),
        (6, "Aproximadamente 30 minutos"),
        (7, "Aproximadamente 45 minutos"),
        (8, "Aproximadamente 1 hora"),
        (9, "Aproximadamente 1 hora e 30 minutos"),
        (10, "Aproximadamente 2 horas"),
        (11, "Acima de 2 horas"),
    )
    quest_aluno_tempo_escola = models.IntegerField('Tempo que o (a) estudante gasta da sua '
                                             'residência ao Campus', choices=QUEST_TEMPO_CAMPUS)

    quest_aluno_gestante = models.BooleanField('Aluna está Gestante? ', default=False)
    quest_aluno_lactante = models.BooleanField('Você é Lactante? ', default=False)
    quest_aluno_medicacao = models.BooleanField('Medicamentos de Uso Regular?', default=False)
    quest_aluno_medicacao_desc = models.CharField('Informe a medicação', max_length=100, null=True, blank=True)
    quest_aluno_medicacao_cid = models.CharField('Informe o CID (Classificação '
                                           'Internacional de Doenças)', max_length=100,
                                           null=True, blank=True)

    def __str__(self):
        return 'Questionário: ' + str(self.questionario_ano) + '/'+ str(self.questionario_semestre)

    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'


class QuestionarioAnexo(Base):
    questionario = models.ForeignKey("Questionario", on_delete=models.PROTECT)
    TIPO_ANEXO = (
        (1, "Valor Gasto com Van"),
        (2, "Valor Gasto com Aluguel ou Financiamento do Imovel"),
        (3, "Valor Gasto com Energia"),
        (4, "Valor Gasto com Água"),
        (5, "Valor Gasto com Conomínio"),
        (6, "Valor Gasto com Medicação"),
    )
    quest_aluno_anexo_tipo = models.IntegerField('Inclua os anexos das suas despesas', choices=TIPO_ANEXO)
    quest_aluno_anexo_valor = models.DecimalField('Informe o valor do anexo', max_digits=8, decimal_places=2)
    quest_aluno_anexo_arq = models.CharField('Anexo/Comprovante', max_length=100)

    def __str__(self):
        return str(self.questionario_id) + str(self.quest_aluno_anexo_tipo) + ' ' + str(self.quest_aluno_anexo_valor)



