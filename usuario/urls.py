from django.urls import path, include
from core.views import IndexView

from .views import PrimeiroAcessoAlunoView, PainelAlunoView
from .views import UsuarioView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('primeiro_acesso_aluno/', PrimeiroAcessoAlunoView.as_view(), name='primeiro_acesso_aluno'),
    #path('painel_aluno/', include('django.contrib.auth.urls')),
    path('painel_aluno/', PainelAlunoView.as_view(), name='painel_aluno'),
]