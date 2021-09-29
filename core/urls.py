from django.urls import path, include

from .views import IndexView, PerguntaFreqView, EquipeView, \
    TodosEditaisView, DetalheEditaisView, DetalhePublicacoesEditaisView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('perguntas_frequente/', PerguntaFreqView.as_view(), name='perguntas_frequente'),
    path('equipe/', EquipeView.as_view(), name='equipe'),
    path('todos_editais/', TodosEditaisView.as_view(), name='todos_editais'),
    path('<int:pk>/detalhe_editais/', DetalheEditaisView.as_view(), name='detalhe_editais'),
    path('detalhe_editais/', DetalhePublicacoesEditaisView.as_view(), name='publicacao_editais'),
]


