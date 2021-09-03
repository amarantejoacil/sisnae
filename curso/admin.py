from django.contrib import admin
from .models import Curso, Semestre


@admin.register(Curso)
class CursoAluno(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'curso_tipo', 'curso_status')  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')

@admin.register(Semestre)
class SemestreAluno(admin.ModelAdmin):
    list_display = ('id', 'semestre',)  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


