from django.urls import path, include


from .views import PrimeiroAcessoAlunoView, PainelAlunoView
from .views import UsuarioView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PainelAlunoView.as_view(), name='painel_aluno'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('primeiro_acesso_aluno/', PrimeiroAcessoAlunoView.as_view(), name='primeiro_acesso_aluno'),
    path('painel_aluno/', PainelAlunoView.as_view(), name='painel_aluno'),
    path('logout/', LogoutView.as_view(), name="logout")
]