from django.contrib import admin
from .models import Edital, PublicacaoEdital

@admin.register(Edital)
class EditalAluno(admin.ModelAdmin):
    list_display = ('descricao', 'numero', 'ano', 'data_hora_inicio', 'data_hora_fim')  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')




@admin.register(PublicacaoEdital)
class EtapaEdital(admin.ModelAdmin):
    list_display = ('publicacao_descricao', 'publicacao_anexo_arq', 'publicacao_data')
