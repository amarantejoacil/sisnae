from django.contrib import admin
from .models import Curso, Semestre


@admin.register(Curso)
class CursoAluno(admin.ModelAdmin):
    list_display = ('id', 'descricao',)  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')

@admin.register(Semestre)
class SemestreAluno(admin.ModelAdmin):
    list_display = ('id', 'semestre',)  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


