from django.shortcuts import render
from django.views.generic import TemplateView


class UsuarioView(TemplateView):
    template_name = 'usuario.html'


class PrimeiroAcessoAlunoView(TemplateView):
    template_name = 'primeiro_acesso_aluno.html'


class PainelAlunoView(TemplateView):
    template_name = 'painel_aluno.html'
