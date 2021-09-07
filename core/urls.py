from django.urls import path

from .views import IndexView, PerguntaFreqView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('perguntas_frequente/', PerguntaFreqView.as_view(), name='perguntas_frequente'),
]