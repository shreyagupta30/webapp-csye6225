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
        self.credentials = base64.b64encode('testinguser@test.com:passwordset'.encode('utf-8')).decode('utf-8')

    def test_create_user(self):
        response = self.api_client.post(self.create_user_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.api_client.credentials(HTTP_AUTHORIZATION='Basic ' + self.credentials)
        response = self.api_client.get(self.get_user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_profile_update(self):
        response = self.api_client.post(self.create_user_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.api_client.credentials(HTTP_AUTHORIZATION='Basic ' + self.credentials)

        #update password, firstname, lastname field
        updated_data = {'password': 'passwordset@123',
                        'firstname': 'test2',
                        'lastname': 'user2'
                        }
        response = self.api_client.put(self.get_user_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        updated_credentials = base64.b64encode('testinguser@test.com:passwordset@123'.encode('utf-8')).decode('utf-8')
        self.api_client.credentials(HTTP_AUTHORIZATION='Basic ' + updated_credentials)
        response = self.api_client.get(self.get_user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #check that update username field is not allowed
        updated_data = {'username': 'testinguser2@test.com'}
        response = self.api_client.put(self.get_user_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
