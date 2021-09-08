from django.contrib import admin
from .models import Inscricao


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'edital', 'inscricao_situacao',
                    'situacao_obs')  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm', 'inscricao_situacao', 'situacao_obs')


   #def __str__(self):
    #    return self.descricao

