from django.contrib import admin
from .models import Questionario


@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id',)  # 'IncEm', 'AltEm', 'IncPor', 'AltPor', 'status_aluno')
    readonly_fields = ('IncPor', 'AltPor', 'IncEm', 'AltEm')


   #def __str__(self):
    #    return self.descricao

