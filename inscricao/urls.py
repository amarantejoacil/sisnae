from django.urls import path

from .views import InscricaoView
urlpatterns = [
    path('', InscricaoView.as_view(), name='InscricaoView'),
]