from django.contrib import admin
from .models import Inscricao, Situacao

@admin.register(Inscricao)
class Inscricao(admin.ModelAdmin):
    list_display = ('situacao_obs', )  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


   #def __str__(self):
    #    return self.descricao

@admin.register(Situacao)
class Situacao(admin.ModelAdmin):
    list_display = ('descricao', 'situacao_status')