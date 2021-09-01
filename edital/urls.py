from django.urls import path

from .views import EditalView
urlpatterns = [
    path('', EditalView.as_view(), name='EditalView'),
]