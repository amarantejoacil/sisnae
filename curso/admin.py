from django.contrib import admin
from .models import Curso, Semestre


@admin.register(Curso)
class CursoAluno(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'curso_tipo', 'curso_status')
    list_display_links = ('id', 'descricao',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')
    list_per_page = 10




@admin.register(Semestre)
class SemestreAluno(admin.ModelAdmin):
    list_display = ('id', 'semestre',)
    list_display_links = ('id', 'semestre',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')
    list_per_page = 10


