from django.urls import path

from .views import ImportacaoView, ListDadosImportacaoView, CreateDadosImportacaoView, ProcessarDadosImportadosView

urlpatterns = [
    path('', ImportacaoView.as_view(), name='ImportacaoView'),
    path('listar-importacao', ListDadosImportacaoView.as_view(), name='ListDadosImportacaoView'),
    path('cadastro-importacao', CreateDadosImportacaoView.as_view(), name='CreateDadosImportacaoView'),
    path('processar/importacao/<int:pk>', ProcessarDadosImportadosView.as_view(), name='ProcessarDadosImportadosView'),
]