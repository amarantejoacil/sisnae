from django.contrib import admin
from .models import Edital, PublicacaoEdital, ModalidadeEdital, SetorEdital

@admin.register(Edital)
class EditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'edital_titulo', 'modalidade_edital', 'numero', 'ano', 'data_hora_inicio',
                    'data_hora_fim', 'setor', 'semestre_edital')
    # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')

@admin.register(PublicacaoEdital)
class PublicacaoEditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'publicacao_descricao', 'publicacao_anexo_arq', 'publicacao_data')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


@admin.register(ModalidadeEdital)
class ModalidadeEditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'modalidade_desc', 'modalidade_status')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


@admin.register(SetorEdital)
class SetorEditalAdmin(admin.ModelAdmin):
    list_display = ('setor_descricao', 'setor_siglas', 'setor_status' )
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


