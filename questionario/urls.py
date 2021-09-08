from django.urls import path

from .views import QuestionarioView
urlpatterns = [
    path('', QuestionarioView.as_view(), name='QuestionarioView'),
]