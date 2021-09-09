from django.urls import path

from .views import PrimeiroAcessoAlunoView
urlpatterns = [
    path('primeiro_acesso_aluno', PrimeiroAcessoAlunoView.as_view(), name='primeiro_acesso_aluno'),
]