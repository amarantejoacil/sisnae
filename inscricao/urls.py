from django.urls import path

from .views import InscricaoView, CreateInscricaoView
urlpatterns = [
    path('', InscricaoView.as_view(), name='InscricaoView'),
    path('cadastro-inscricao/', CreateInscricaoView.as_view(), name='CreateInscricaoView'),
]