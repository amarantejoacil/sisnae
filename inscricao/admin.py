from django.contrib import admin
from .models import Inscricao

@admin.register(Inscricao)
class Inscricao(admin.ModelAdmin):
    list_display = ('situacao_obs', )  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')


   #def __str__(self):
    #    return self.descricao