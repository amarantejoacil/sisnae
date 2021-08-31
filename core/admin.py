from django.contrib import admin
from .models import Pessoa, Aluno, Cidade, Banco



@admin.register(Pessoa)
class AdminPessoa(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'pessoa_status')


@admin.register(Aluno)
class AdminAluno(admin.ModelAdmin):
    list_display = ('matricula', )  #'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


@admin.register(Cidade)
class AdminCidade(admin.ModelAdmin):
    list_display = ('descricao', 'cidade_status', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )


@admin.register(Banco)
class AdminBanco(admin.ModelAdmin):
    list_display = ('descricao', 'banco_status', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )





