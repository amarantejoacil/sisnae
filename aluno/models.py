from django.db import models
from core.models import Pessoa
from curso.models import Curso, Semestre



class Aluno(models.Model):
    aluno_status = models.BooleanField('Aluno ativo? ', default=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    semestre = models.ForeignKey(Semestre, on_delete=models.PROTECT)
    aluno_matricula = models.BigIntegerField('Matricula', unique=True)
    IncPor = models.BigIntegerField('Incluido Por', null=True, blank=True)
    AltPor = models.BigIntegerField('Alterado Por', null=True, blank=True)
    IncEm = models.DateTimeField('Incluido Em', auto_now_add=True)
    AltEm = models.DateTimeField('Alterado Em', auto_now=True)
    aluno_revisar_cadastro = models.BooleanField('Forçar o aluno Revisar cadastro?', default=False, null=True,
                                                  blank=True)

    def __str__(self):
        return "{} - Matrícula: {} - Curso:{}".format(self.pessoa.nome, self.aluno_matricula, self.curso.descricao)
        # return str(self.aluno_matricula)

