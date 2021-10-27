from django.views.generic import TemplateView, CreateView, ListView


class InscricaoView(ListView):
    template_name = 'inscricao.html'


class CreateInscricaoView(CreateView):
    template_name = 'formularios/form_basic.html'



