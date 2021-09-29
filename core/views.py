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
    paginate_by = 10
    ordering = '-id'


class DetalheEditaisView(DetailView):
    model = Edital
    template_name = 'detalhe_editais.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalhe_editais'] = Edital.objects.all()
        # print('context-----------------------')
        # print(context)
        return context

class DetalhePublicacoesEditaisView(ListView):
    #modelo 3
    model = PublicacaoEdital
    template_name = 'detalhe_editais.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalhe_publicacoes'] = PublicacaoEdital.objects.all()
        print('context-----------------------')
        print(context)
        return context









    # modelo 2 listview
    # model = PublicacaoEdital
    # paginate_by = 20
    # template_name = 'detalhe_editais.html'
    # queryset = PublicacaoEdital.objects.all()
    # print('queryset-----------------------')
    # print(queryset)
    # context_object_name = 'publicacao_editais'
    # print(context_object_name)


    #modelo 1
    # model = PublicacaoEdital
    # paginate_by = 20 #usando no listview
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['publicacao'] = PublicacaoEdital.objects.all()
    #     print(context)
    #     return context











