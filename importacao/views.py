from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Importacao
from django.urls import reverse_lazy
import pandas as pd


class ImportacaoView(TemplateView):
    template_name = 'importacao.html'


class CreateDadosImportacaoView(CreateView):
    model = Importacao
    fields = ['id', 'descricao', 'arquivo', 'semestre', 'ano' ]
    template_name = '../templates/cadastros/form-upload.html'
    success_url = reverse_lazy('ListDadosImportacaoView')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Importação'
        context['botao'] = 'Cadastrar'
        context['botao-voltar'] = 'ListDadosImportacaoView'
        # enviando um html para view...
        # anotação no formhtml autoscape força intepretar o html
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        return context

    def form_valid(self, form):
        # obs1. antes do super o objeto com dados não foi criado

        # pegando a instancia do meu usuario do models na hora do formulario
        form.instance.usuario = self.request.user

        # super = força a chamar o form_valid do createview
        url = super().form_valid(form)

        print(self.object.arquivo)
        # obs2. depois do super o objeto com os dados foi criado

        return url


class ListDadosImportacaoView(ListView):
    model = Importacao
    template_name = 'list-importacao.html'
    paginate_by = 10
    ordering = '-id'


class ProcessarDadosImportadosView(DetailView):
    model = Importacao
    login_url = reverse_lazy('ListDadosImportacaoView')





    # def get_queryset(self):
        # self.object_lista = Importacao.objects.all()
        # return self.object_lista



