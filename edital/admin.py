from django.contrib import admin
from .models import Edital, PublicacaoEdital, ModalidadeEdital, SetorEdital

@admin.register(Edital)
class EditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'edital_titulo', 'modalidade_edital', 'numero', 'ano', 'data_hora_inicio',
                    'data_hora_fim', 'setor', 'semestre_edital', 'edital_quantidade_vaga', 'edital_valor_auxilio')
    list_display_links = ('id', 'edital_titulo',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')
    list_per_page = 10

@admin.register(PublicacaoEdital)
class PublicacaoEditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'publicacao_descricao', 'publicacao_anexo_arq', 'publicacao_data')
    list_display_links = ('id', 'publicacao_descricao',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')
    list_per_page = 10


@admin.register(ModalidadeEdital)
class ModalidadeEditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'modalidade_desc', 'modalidade_status')
    list_display_links = ('id', 'modalidade_desc',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')
    list_per_page = 10


@admin.register(SetorEdital)
class SetorEditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'setor_descricao', 'setor_siglas', 'setor_status' )
    list_display_links = ('id', 'setor_descricao',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


