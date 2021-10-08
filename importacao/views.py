from django.views.generic import TemplateView, ListView
from .models import Importacao
from django.urls import reverse_lazy


class ImportacaoView(TemplateView):
    template_name = 'importacao.html'


class CreateDadosImportacaoView(ListView):
    login_url = reverse_lazy('index')
    model = Importacao
    fields = ['id', 'descricao', 'arquivo', ]
    template_name = 'form-upload.html'
    success_url = reverse_lazy('ListDadosImportacaoView')


class ListDadosImportacaoView(ListView):
    model = Importacao
    template_name = 'list-importacao.html'
    paginate_by = 10
    ordering = '-id'

