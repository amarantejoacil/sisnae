from django.contrib import admin
from .models import Edital

@admin.register(Edital)
class EditalAluno(admin.ModelAdmin):
    list_display = ('descricao', 'numero', 'ano', 'data_inicio', 'data_fim')  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


