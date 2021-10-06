from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Edital, PublicacaoEdital


class EditalView(TemplateView):
    template_name = 'edital.html'


class TodosEditaisView(ListView):
    model = Edital
    template_name = 'todos_editais.html'
    paginate_by = 10
    ordering = '-id'


class DetalheEditaisView(DetailView):
    model = Edital
    template_name = 'detalhe_editais.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['detalhe_editais'] = Edital.objects.all()
        context['publicacao'] = PublicacaoEdital.objects.all()
        return context


