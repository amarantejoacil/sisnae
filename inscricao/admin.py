from django.contrib import admin
from .models import Inscricao, Situacao, Modalidade

@admin.register(Inscricao)
class Inscricao(admin.ModelAdmin):
    list_display = ('situacao_obs', )  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


   #def __str__(self):
    #    return self.descricao

@admin.register(Situacao)
class Situacao(admin.ModelAdmin):
    list_display = ('descricao', 'situacao_status')


@admin.register(Modalidade)
class ModalidadeAluno(admin.ModelAdmin):
    list_display = ('modalidade_desc', 'modalidade_status' )
