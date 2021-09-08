from django.contrib import admin
from .models import Questionario, QuestionarioAnexo


@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'edital_id',)  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


   #def __str__(self):
    #    return self.descricao

@admin.register(QuestionarioAnexo)
class QuestionarioAnexoAdmin(admin.ModelAdmin):
    aluno_anexo_tipo = ('id', 'quest_aluno_anexo_tipo', 'quest_aluno_anexo_valor' 'IncEm', 'AltEm', 'IncPor', 'AltPor')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')

