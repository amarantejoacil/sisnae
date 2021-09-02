from django.db import models
from core.models import Pessoa, Base
from curso.models import Curso, Semestre


from stdimage.models import StdImageField
from django.contrib.auth import get_user_model

class Aluno(models.Model):
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
        (11, "acima de 30km"),
    )

    aluno_dist_escola = models.IntegerField('Distância aproximada da residência ao Campus Várzea Grande em KM?',
                                            choices=DISTANCIA_RESIDENCIA)


    aluno_status = models.BooleanField('Aluno ativo? ', default=True)


    def __str__(self):
        return str(self.aluno_matricula)



class Modalidade(Base):
    modalidade_desc = models.CharField('Descricao', max_length=100)
    modalidade_status = models.BooleanField('Modalidade ativa?', default=True)

    def __str__(self):
        return str(self.modalidade_desc)