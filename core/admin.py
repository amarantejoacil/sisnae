
from django.contrib import admin
from .models import Pessoa, Aluno

@admin.register(Pessoa)
class AdminPessoa(admin.ModelAdmin):
    list_display = ('nome', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )


@admin.register(Aluno)
class AdminAluno(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )






