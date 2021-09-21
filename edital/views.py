from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Edital


class EditalView(TemplateView):
    template_name = 'edital.html'


# class EditalList(ListView):
#     models = Edital
#     template_name = 'detalhe_editais'
#     queryset = Edital.objects.all()
#     context_object_name = 'context_detalhe_editais'

