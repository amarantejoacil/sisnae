from django.urls import path

from .views import CursoView
urlpatterns = [
    path('', CursoView.as_view(), name='CursoView'),
]