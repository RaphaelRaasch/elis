from django.contrib import admin
from .models import Formacao


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao','concluido')
