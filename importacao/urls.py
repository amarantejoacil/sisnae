from django.urls import path

from .views import ImportacaoView

urlpatterns = [
    path('', ImportacaoView.as_view(), name='ImportacaoView'),
]