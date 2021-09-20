from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AdminAluno(admin.ModelAdmin):
    list_display = ('get_nome', 'aluno_matricula', 'aluno_status', 'curso',)#, 'IncEm', 'AltEm', 'IncPor', 'AltPor')
    list_display_links = ('get_nome', 'aluno_matricula')
    search_fields = ('aluno_matricula',)
    list_filter = ('aluno_matricula',)
    #list_editable = ('pessoa_status',)
    list_per_page = 15

    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')

    def get_nome(self, obj):

        return obj.pessoa.nome
    get_nome.short_description = 'Nome'






