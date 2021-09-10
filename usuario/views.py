import django.views.generic
from django.shortcuts import render
from django.views.generic import TemplateView, FormView


from .forms import UsuarioForm
from django.urls import reverse_lazy


class UsuarioView(TemplateView):
    template_name = 'usuario.html'


class PrimeiroAcessoAlunoView(FormView):
    template_name = 'primeiro_acesso_aluno.html'
    form_class = UsuarioForm
    #success_url = '/acesso/painel_aluno'
    success_url = reverse_lazy('painel_aluno')

    """ 
    def valida_dados(request):
        if request.method == 'POST':
            matricula = request.POST['matricula']
            print(matricula)
        else:
            print(aa)
    """



class PainelAlunoView(TemplateView):
    template_name = 'painel_aluno.html'


class LogoutView(TemplateView):
    template_name = 'index.html'
