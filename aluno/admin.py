from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AdminAluno(admin.ModelAdmin):
    list_display = ('id', 'aluno_matricula', 'aluno_status')#, 'IncEm', 'AltEm', 'IncPor', 'AltPor')
    list_display_links = ('aluno_matricula', )
    search_fields = ('aluno_matricula',)
    list_filter = ('aluno_matricula', 'aluno_status')
    #list_editable = ('pessoa_status',)
    list_per_page = 15

    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')



