from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
import base64

class TestIntegration(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.create_user_url = reverse('user_auth')
        cls.get_user_url = reverse('user_self')

    def setUp(self):
        self.api_client = APIClient()
        self.user_data = {
            'username': 'testinguser@test.com',
            'password': 'passwordset',
            'firstname': 'test',
            'lastname': 'user',
        }

    def test_create_user(self):
        response = self.api_client.post(self.create_user_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
