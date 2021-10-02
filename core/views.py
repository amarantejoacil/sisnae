from django.views.generic import TemplateView, ListView, DetailView
from edital.models import Edital, PublicacaoEdital
from django.shortcuts import get_object_or_404


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['detalhe_editais'] = Edital.objects.all()
        context['publicacao'] = PublicacaoEdital.objects.all()
        # print('context-----------------------')
        # print(context)
        return context

class DetalhePublicacoesEditaisView(ListView):

    model = PublicacaoEdital
    template_name = 'detalhe_editais.html'



    # def get_queryset(self):
    #     #self.object_lista = Atividade.objects.all()
    #     self.object_lista = PublicacaoEdital.objects.all()
    #     print(self.object_lista)
    #     return self.object_lista



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['publicacao'] = PublicacaoEdital.objects.all()
    #     print('c' + str(context))
    #     return context





    #modelo 2 listview
    # model = PublicacaoEdital
    # paginate_by = 20
    # template_name = 'detalhe_editais.html'
    #
    # def get_queryset(self):
    #     self.object_lista = PublicacaoEdital.objects.all()
    #     print('object_lista' + str(self.object_lista))
    #     return self.object_lista


    #modelo 1
    # model = PublicacaoEdital
    # paginate_by = 20 #usando no listview
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['publicacao'] = PublicacaoEdital.objects.all()
    #     print(context)
    #     return context


    #modelo 04
    # model = PublicacaoEdital
    # template_name = 'detalhe_editais.html'
    #
    # def get_queryset(self):
    #     self.object_lista = PublicacaoEdital.objects.all()
    #     return self.object_lista



    #modelo 3
    # model = PublicacaoEdital
    # template_name = 'detalhe_editais.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['detalhe_publicacoes'] = PublicacaoEdital.objects.all()
    #     print('context-----------------------')
    #     print(context)
    #     return context

















