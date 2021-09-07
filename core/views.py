from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class PerguntaFreqView(TemplateView):
    template_name = 'perguntas_frequente.html'