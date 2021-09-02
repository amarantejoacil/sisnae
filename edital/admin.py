from django.contrib import admin
from .models import Edital, PublicacaoEdital, ModalidadeEdital, SetorEdital

@admin.register(Edital)
class EditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'numero', 'ano', 'data_hora_inicio', 'data_hora_fim')  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


@admin.register(PublicacaoEdital)
class PublicacaoEditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'publicacao_descricao', 'publicacao_anexo_arq', 'publicacao_data')


@admin.register(ModalidadeEdital)
class ModalidadeEditalAdmin(admin.ModelAdmin):
    list_display = ('id', 'modalidade_desc', 'modalidade_status' )


@admin.register(SetorEdital)
class SetorEditalAdmin(admin.ModelAdmin):
    list_display = ('setor_descricao', 'setor_siglas', 'setor_status' )


