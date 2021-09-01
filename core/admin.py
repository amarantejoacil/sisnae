from django.contrib import admin
from .models import Pessoa, Cidade, Banco



@admin.register(Pessoa)
class AdminPessoa(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cidade', 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'pessoa_status')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_filter = ('cidade', 'pessoa_status')
    list_editable = ('pessoa_status', )
    list_per_page = 15

@admin.register(Cidade)
class AdminCidade(admin.ModelAdmin):
    list_display = ('descricao', 'cidade_status', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )


@admin.register(Banco)
class AdminBanco(admin.ModelAdmin):
    list_display = ('descricao', 'banco_status', 'IncEm', 'AltEm', 'IncPor', 'AltPor', )





