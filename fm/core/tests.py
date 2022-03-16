from django.test import TestCase


class HomeTeste(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """GET / must return template index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
