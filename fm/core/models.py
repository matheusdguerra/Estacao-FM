from tabnanny import verbose
from django.db import models


class Stations(models.Model):
    entidade = models.CharField('Nome da entidade', max_length=100)
    uf = models.CharField('Estado', max_length=2)
    localidade = models.CharField('Localidade', max_length=50)
    frequencia = models.CharField('Frequência', max_length=50)

    class Meta:
        verbose_name_plural = 'estação FM'
        verbose_name = 'estação FM'

    def __str__(self):
        return self.entidade
