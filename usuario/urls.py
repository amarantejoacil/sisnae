from django.urls import path, include


from .views import UsuarioCreate
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', PainelLoginAlunoView.as_view(), name='painel_login_aluno'),

    # se a url for só /acesso chama painel_login_aluno
    path('registrar_aluno/', UsuarioCreate.as_view(), name='registrar_aluno'),

    path('painel_login_aluno/', auth_views.LoginView.as_view(
        template_name='painel_login_aluno.html'
    ), name='painel_login_aluno'),

    path('logout/', auth_views.LogoutView.as_view(), name="logout")
]