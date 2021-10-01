from django.contrib import admin
from .models import Inscricao


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('id','aluno', 'edital', 'inscricao_situacao', 'questionario',
                    'situacao_obs')
    list_display_links = ('id', 'aluno', 'edital',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm', 'inscricao_situacao', 'situacao_obs')
    list_per_page = 10


