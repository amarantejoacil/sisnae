from django.contrib import admin
from .models import Aluno, Modalidade

@admin.register(Aluno)
class AdminAluno(admin.ModelAdmin):
    list_display = ('matricula', 'aluno_status' )  #'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


@admin.register(Modalidade)
class ModalidadeAluno(admin.ModelAdmin):
    list_display = ('modalidade_desc', 'modalidade_status' )