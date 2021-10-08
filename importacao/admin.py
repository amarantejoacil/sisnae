from django.contrib import admin
from .models import Importacao


@admin.register(Importacao)
class ImportacaoAdmin(admin.ModelAdmin):
    list_display = ('id','descricao', 'arquivo', 'situacao', 'ano', 'semestre')
    list_display_links = ('id','descricao', 'arquivo',)
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm',)
    list_per_page = 10


