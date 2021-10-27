from django.contrib import admin
from .models import Inscricao, QuestionarioAnexo


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('id','aluno', 'edital', 'inscricao_situacao', 'situacao_obs')
    list_display_links = ('id', 'aluno', 'edital',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm', 'inscricao_situacao', 'situacao_obs')
    list_per_page = 10


@admin.register(QuestionarioAnexo)
class QuestionarioAnexoAdmin(admin.ModelAdmin):
    list_display = ('id', 'inscricao', 'quest_aluno_anexo_tipo', 'quest_aluno_anexo_valor', 'quest_aluno_anexo_arq')
    list_display_links = ('id', 'inscricao', 'quest_aluno_anexo_tipo',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm',)
    list_per_page = 10


