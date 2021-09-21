from django.views.generic import TemplateView, ListView
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


class TodosEditaisView(ListView):
    model = Edital
    template_name = 'todos_editais.html'
    paginate_by = 3
    ordering = 'id'


class DetalheEditaisView(ListView):
    models = Edital
    template_name = 'detalhe_editais.html'
    queryset = Edital.objects.all()
    # queryset = Edital.objects.filter(id=1)
    context_object_name = 'detalhe_editais'





