from django.contrib import admin

from .models import Atendido, Avaliador, Responsavel

admin.site.register(Atendido)
admin.site.register(Avaliador)
admin.site.register(Responsavel)

