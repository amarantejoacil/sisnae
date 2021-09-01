from django.contrib import admin
from .models import Curso, Semestre


@admin.register(Curso)
class CursoAluno(admin.ModelAdmin):
    list_display = ('descricao',)  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')

@admin.register(Semestre)
class SemestreAluno(admin.ModelAdmin):
    list_display = ('semestre',)  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


