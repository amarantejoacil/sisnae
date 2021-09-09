from django.urls import path
from core.views import IndexView

from .views import PrimeiroAcessoAlunoView
urlpatterns = [
    path('', IndexView.as_view(), name='primeiro_acesso_aluno'),
    path('primeiro_acesso_aluno', PrimeiroAcessoAlunoView.as_view(), name='primeiro_acesso_aluno'),
]