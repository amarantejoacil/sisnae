from django.views.generic import TemplateView, ListView, DetailView
from edital.models import Edital, PublicacaoEdital


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['editais'] = Edital.objects.all()
        return context


class PerguntaFreqView(TemplateView):
    template_name = 'perguntas_frequente.html'


class EquipeView(TemplateView):
    template_name = 'equipe.html'


class TodosEditaisView(ListView):
    model = Edital
    template_name = 'todos_editais.html'
    paginate_by = 3
    ordering = 'id'


class DetalheEditaisView(DetailView):
    model = Edital
    template_name = 'detalhe_editais.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalhe_editais'] = Edital.objects.all()
        return context

class DetalhePublicacoesEditaisView(DetailView):
    model = PublicacaoEdital
    template_name = 'detalhe_editais.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicacao_detalhe_editais'] = PublicacaoEdital.objects.all()
        return context







