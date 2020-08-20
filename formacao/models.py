from django.db import models


class Formacao(models.Model):
    instituicao = models.CharField('Instituição', max_length=155)
    status = models.IntegerField('Status')
    concluido = models.IntegerField('Concluido')
    titulo = models.CharField('Titulo', max_length=155)

    def __str__(self):
        return self.titulo
