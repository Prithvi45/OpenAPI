from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .schema import DUMMY_DATA

from .models import DummyData #ref purpose, mock simulates for testing purpose
from unittest.mock import patch



class DummyDataAPITests(APITestCase):
    def setUp(self):
        # Initialize data before tests
        self.list_url = reverse('dummy-data-list')
        self.detail_url = lambda pk: reverse('dummydata-detail', args=[pk])

    def test_list_dummy_data(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['data'], list)
        print("Test case 1")

    @patch('DataApp.models.DummyData')  # Replace 'your_app' with the actual app name
    def test_create_dummy_data(self, MockDummyData):
        # Configure the mock instance
        mock_instance = MockDummyData.return_value
        mock_instance.name = 'Test User'
        mock_instance.datetime = '2024-12-19T12:34:56'

        # Simulate the create method
        MockDummyData.objects.create.return_value = mock_instance

        # Perform the API request
        url = reverse('dummy-data-list')  # Ensure this URL name matches your URL configuration
        data = {'name': 'Test User', 'datetime': '2024-12-19T12:34:56'}
        response = self.client.post(url, data, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test User') 
        print("test case 2")
'''
    def test_retrieve_dummy_data(self):
        dummy = DummyData.objects.create(name='Test User', datetime='2024-12-19T12:34:56')
        response = self.client.get(self.detail_url(dummy.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test User')

    def test_update_dummy_data(self):
        dummy = DummyData.objects.create(name='Test User', datetime='2024-12-19T12:34:56')
        updated_data = {'name': 'Updated User', 'datetime': '2024-12-20T12:34:56'}
        response = self.client.put(self.detail_url(dummy.pk), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])

    def test_delete_dummy_data(self):
        dummy = DummyData.objects.create(name='Test User', datetime='2024-12-19T12:34:56')
        response = self.client.delete(self.detail_url(dummy.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(DummyData.objects.filter(pk=dummy.pk).exists())
'''
