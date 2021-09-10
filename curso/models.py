from django.db import models
from core.models import Base


class Curso(Base):
    descricao = models.CharField('Descrição', max_length=100)
    semestre = models.ManyToManyField("Semestre")
    CURSO_TIPO = (
        (1, "Técnico"),
        (2, "Graduação"),
        (3, "Especialização"),
        (4, "Mestrado"),
        (5, "Doutorado"),
    )
    curso_tipo = models.IntegerField('Tipo do Curso', choices=CURSO_TIPO)

    curso_status = models.BooleanField('Curso ativo?', default=True)


    def __str__(self):
        return self.descricao


class Semestre(Base):
    semestre_status = models.BooleanField('Semestre ativo?', default=True)
    SEMESTRE_CHOICES = (
        (1, "1° Semestre"),
        (2, "2° Semestre"),
        (3, "3° Semestre"),
        (4, "4° Semestre"),
        (5, "5° Semestre"),
        (6, "6° Semestre"),
        (7, "7° Semestre"),
        (8, "8° Semestre"),
        (9, "9° Semestre"),
        (10, "10° Semestre"),
    )
    semestre = models.IntegerField('Semestre', choices=SEMESTRE_CHOICES)


    def __str__(self):
        return str(self.semestre) + "° SEMESTRE"