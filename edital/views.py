from django.views.generic import TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Edital


class EditalView(TemplateView):
    template_name = 'edital.html'


