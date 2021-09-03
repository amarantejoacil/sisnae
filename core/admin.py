from django.contrib import admin
from .models import Pessoa, Cidade, Banco



@admin.register(Pessoa)
class AdminPessoa(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'email', 'data_nascimento', 'pessoa_status')
    list_display_links = ('id', 'nome', 'cpf')
    search_fields = ('nome', 'cpf')
    list_filter = ('cidade', 'pessoa_status')
    list_editable = ('pessoa_status', )
    list_per_page = 15
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')

@admin.register(Cidade)
class AdminCidade(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'cidade_status', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


@admin.register(Banco)
class AdminBanco(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'banco_status', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')





