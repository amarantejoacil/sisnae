from django.urls import path

from .views import EditalView, TodosEditaisView, DetalheEditaisView
urlpatterns = [
    path('', EditalView.as_view(), name='EditalView'),
    path('todos_editais/', TodosEditaisView.as_view(), name='todos_editais'),
    path('<int:pk>/detalhe_editais/', DetalheEditaisView.as_view(), name='detalhe_editais'),
]