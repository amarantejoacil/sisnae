from django.urls import path

from .views import IndexView, PerguntaFreqView, EquipeView, PainelEstudanteView, TodosEditaisView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('perguntas_frequente/', PerguntaFreqView.as_view(), name='perguntas_frequente'),
    path('equipe/', EquipeView.as_view(), name='equipe'),
    path('painel_estudante/', PainelEstudanteView.as_view(), name='painel_estudante'),
    path('todos_editais/', TodosEditaisView.as_view(), name='todos_editais'),
]