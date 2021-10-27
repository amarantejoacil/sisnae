import django.views.generic
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from core.models import Pessoa
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin



from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import UsuarioForm


# class PrimeiroAcessoAlunoView(CreateView):
#     template_name = 'registrar_aluno.html'
#     form_class = UsuarioForm
#     success_url = reverse_lazy('painel_login_aluno')


class PainelLoginAlunoView(TemplateView):
    template_name = 'painel_login_aluno.html'


class PainelAlunoView(TemplateView):
    template_name = 'painel_aluno.html'

#
# class LogoutView(TemplateView):
#     template_name = 'index.html'


class UsuarioCreate(CreateView):
    template_name = 'registrar_aluno.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('painel_login_aluno')

