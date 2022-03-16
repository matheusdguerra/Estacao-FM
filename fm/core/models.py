from django.db import models


class Stations(models.Model):
    entidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    localidade = models.CharField(max_length=50)
    frequencia = models.CharField(max_length=50)
