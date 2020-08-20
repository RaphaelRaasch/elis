from django.db import models

from formacao.models import Formacao


class Psicologo(models.Model):
    numCRP = models.IntegerField('CRP')
    formacao = models.ManyToManyField(Formacao)

    def __str__(self):
        return f'{self.numCRP}'
