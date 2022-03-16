from django.test import TestCase
from fm.core.models import Stations


class StationModelTest(TestCase):
    def setUp(self):
        self.obj = Stations(
            entidade='Rádio Liberdade',
            uf='RS',
            localidade='Porto Alegre',
            frequencia='83,3 MHz'
        )

    def teste_create(self):
        self.obj.save()
        self.assertTrue(Stations.objects.exists())
