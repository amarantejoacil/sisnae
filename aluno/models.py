from django.db import models
from core.models import Pessoa, Base
from curso.models import Curso, Semestre


from stdimage.models import StdImageField
from django.contrib.auth import get_user_model

class Aluno(models.Model):
    aluno_status = models.BooleanField('Aluno ativo? ', default=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.RESTRICT)
    semestre = models.ForeignKey(Semestre, on_delete=models.RESTRICT)
    aluno_matricula = models.BigIntegerField('Matricula', unique=True)

    FORMA_INGRESSO_CHOICES = (
        ('A', "Por Ampla Concorrência"),
        ('C', "Por Meio de Cota"),
    )
    aluno_form_ingre = models.CharField('Forma de Ingresso', choices=FORMA_INGRESSO_CHOICES, max_length=1)


    DISTANCIA_RESIDENCIA = (
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
    aluno_dist_escola = models.IntegerField('Distância aproximada da residência ao Campus em KM?',
                                            choices=DISTANCIA_RESIDENCIA)

    TRANSPORTE_CAMPUS = (
        (1, "Transporte Coletivo"),
        (2, "Van"),
        (3, "Carro"),
        (4, "Moto"),
        (5, "A pé"),
        (6, "Carona"),
        (7, "Bicicleta"),
    )

    aluno_transporte = models.IntegerField('Informe o meio de transporte '
                                           'utilizado para chegar ao Campus?', choices=TRANSPORTE_CAMPUS)



    TEMPO_CAMPUS = (
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
    aluno_tempo_escola = models.IntegerField('Tempo que o (a) estudante gasta da sua '
                                             'residência ao Campus', choices=TEMPO_CAMPUS)

    aluno_gestante = models.BooleanField('Aluna está Gestante? ', default=False)
    aluno_lactante = models.BooleanField('Você é Lactante? ', default=False)
    aluno_medicacao = models.BooleanField('Medicamentos de Uso Regular?', default=False)
    aluno_medicacao_desc = models.CharField('Informe a medicação', max_length=100, null=True, blank=True)
    aluno_medicacao_cid = models.CharField('Informe o CID (Classificação '
                                           'Internacional de Doenças)', max_length=100,
                                           null=True, blank=True)


    IncPor = models.IntegerField('Incluido Por', null=True, blank=True)
    AltPor = models.IntegerField('Alterado Por', null=True, blank=True)
    IncEm = models.DateTimeField('Incluido Em', auto_now_add=True)
    AltEm = models.DateTimeField('Alterado Em', auto_now=True)




    def __str__(self):
        return str(self.aluno_matricula)



class AlunoAnexo(Base):
    aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE)
    TIPO_ANEXO = (
        (1, "Valor Gasto com Van"),
        (2, "Valor Gasto com Aluguel ou Financiamento do Imovel"),
        (3, "Valor Gasto com Energia"),
        (4, "Valor Gasto com Água"),
        (5, "Valor Gasto com Conomínio"),
        (6, "Valor Gasto com Medicação"),
    )
    aluno_anexo_tipo = models.IntegerField('Inclua os anexos das suas despesas', choices=TIPO_ANEXO)
    aluno_anexo_valor = models.DecimalField('Informe o valor do anexo', max_digits=8, decimal_places=2)
    aluno_anexo_arq = models.CharField('Anexo/Comprovante', max_length=100)

    def __str__(self):
        return str(self.aluno_anexo_tipo)