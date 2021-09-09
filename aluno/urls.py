from django.urls import path

from .views import AlunoView
urlpatterns = [
    path('primeiro_acesso', AlunoView.as_view(), name='AlunoView'),
]