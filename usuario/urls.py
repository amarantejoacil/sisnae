from django.urls import path, include


from .views import PrimeiroAcessoAlunoView, PainelLoginAlunoView
from .views import UsuarioView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PainelLoginAlunoView.as_view(), name='painel_login_aluno'),
    # se a url for só /acesso chama painel_login_aluno

    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('primeiro_acesso_aluno/', PrimeiroAcessoAlunoView.as_view(), name='primeiro_acesso_aluno'),
    # path('primeiro_acesso_aluno/', auth_views.LoginView.as_view(
    #     template_name='primeiro_acesso_aluno.html'
    # ) , name='primeiro_acesso_aluno'),

    path('painel_login_aluno/', auth_views.LoginView.as_view(
        template_name='painel_login_aluno.html'
    ), name='painel_login_aluno'),
    # path('painel_aluno/', PainelAlunoView.as_view(), name='painel_aluno'),


    path('logout/', LogoutView.as_view(), name="logout")
]