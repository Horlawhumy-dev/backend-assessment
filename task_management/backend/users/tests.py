from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserAuthTests(APITestCase):
    def test_register(self):
        url = "/api/users/register/"
        data = {
            'username': 'testuser', 
            'email': 'testuser@example.com', 
            'password': 'testpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login(self):
        # Create a user before attempting to log in
        User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        
        url = "/api/users/login/"
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)