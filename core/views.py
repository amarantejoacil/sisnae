from django.views.generic import TemplateView
from edital.models import Edital


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


class TodosEditaisView(TemplateView):
    template_name = 'todos_editais.html'

    def get_context_data(self, **kwargs):
        context = super(TodosEditaisView, self).get_context_data(**kwargs)
        context['editais'] = Edital.objects.all()

        return context


class DetalheEditaisView(TemplateView):
    template_name = 'detalhe_editais.html'




