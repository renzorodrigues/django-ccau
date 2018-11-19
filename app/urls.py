"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework import routers
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.schemas import get_schema_view
from usuario.api.viewsets import AtendidoViewSet
from usuario.api.viewsets import AvaliadorViewSet
from usuario.api.viewsets import ResponsavelViewSet
from unidade.api.viewsets import UnidadeViewSet
from avaliacao.api.viewsets import AvaliacaoViewSet
from turma.api.viewsets import TurmaViewSet
# from turma.api.viewsets import PeriodoViewSet

router = routers.DefaultRouter()
router.register(r'atendidos', AtendidoViewSet)
router.register(r'avaliadores', AvaliadorViewSet)
router.register(r'responsaveis', ResponsavelViewSet)
router.register(r'unidades', UnidadeViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)
router.register(r'turmas', TurmaViewSet)
# router.register(r'periodos', PeriodoViewSet)

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('docs/', schema_view)
]
