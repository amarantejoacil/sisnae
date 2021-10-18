from django.views.generic import TemplateView, ListView, DetailView
from edital.models import Edital, PublicacaoEdital
from django.shortcuts import get_object_or_404


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['editais'] = Edital.objects.filter(edital_status=True).order_by('-id')[:12]
        return context

class PerguntaFreqView(TemplateView):
    template_name = 'perguntas_frequente.html'


class EquipeView(TemplateView):
    template_name = 'equipe.html'

