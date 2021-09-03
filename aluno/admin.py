from django.contrib import admin
from .models import Aluno, AlunoAnexo

@admin.register(Aluno)
class AdminAluno(admin.ModelAdmin):
    list_display = ('aluno_matricula', 'aluno_status' )  #'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')
    list_display_links = ('aluno_matricula', )
    search_fields = ('aluno_matricula',)
    list_filter = ('aluno_matricula', 'aluno_status')
    #list_editable = ('pessoa_status',)
    list_per_page = 15

    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')

@admin.register(AlunoAnexo)
class AdminAlunoAnexo(admin.ModelAdmin):
    aluno_anexo_tipo = ('aluno_anexo_tipo', 'aluno_anexo_valor' 'IncEm', 'AltEm', 'IncPor', 'AltPor')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')
