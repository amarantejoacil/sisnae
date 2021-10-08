"""sisnae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('aluno/', include('aluno.urls')),
    path('curso/', include('curso.urls')),
    path('edital/', include('edital.urls')),
    path('inscricao/', include('inscricao.urls')),
    path('acesso/', include('usuario.urls')),
    path('importacao/', include('importacao.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.AdminSite.site_header = 'SISNAE - VGD'
admin.AdminSite.site_title = 'Sistema do Núcleo de Assistência Estudantil'
admin.AdminSite.index_title = 'Sistema do Núcleo de Assistência Estudantil'
