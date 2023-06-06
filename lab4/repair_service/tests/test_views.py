from django.test import TestCase
import requests

from repair_service.models import Service


class RepairServiceViewsTestClass(TestCase):

    def test_home_page(self):
        url = 'http://localhost:8000/'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_service_list_page(self):
        url = 'http://localhost:8000/services'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_service_detail_page_should_return_forbidden(self):
        Service.objects.first()
        url = 'http://localhost:8000/card/add/'
        response = requests.post(url)
        self.assertEqual(response.status_code, 403)
