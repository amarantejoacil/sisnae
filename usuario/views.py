import django.views.generic
from django.shortcuts import render
from django.views.generic import TemplateView, FormView


from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import UsuarioForm


class UsuarioView(TemplateView):
    template_name = 'usuario.html'


class PrimeiroAcessoAlunoView(CreateView):
    template_name = 'primeiro_acesso_aluno.html'
    form_class = UsuarioForm
    # fields = ['username', 'email', 'password']
    # success_url = '/acesso/painel_aluno'
    success_url = reverse_lazy('painel_aluno')




class PainelLoginAlunoView(TemplateView):
    template_name = 'painel_login_aluno.html'


class LogoutView(TemplateView):
    template_name = 'index.html'
