from django.test import TestCase
from fm.core.models import Stations


class StationModelTest(TestCase):
    def setUp(self):
        self.obj = Stations(
            entidade='Rádio Aliança',
            uf='RS',
            localidade='Porto Alegre',
            frequencia='106,3 MHz'
        )

    def teste_create(self):
        self.obj.save()
        self.assertTrue(Stations.objects.exists())

    def test_str(self):
        self.assertEqual('Rádio Aliança', str(self.obj))
