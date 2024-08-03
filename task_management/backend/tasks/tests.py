from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Generate token for the user
        self.token = Token.objects.create(user=self.user)

        # Include the token in the headers
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_create_task(self):
        url = '/api/tasks/'  # Direct URL for creating and listing tasks
        data = {
            'title': 'Task 1', 
            'description': 'Test task', 
            'status': 'pending', 
            'due_date': '2024-08-31'
        }
        response = self.client.post(url, data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        Task.objects.create(
            title='Task 1', description='Test task', status='pending', due_date='2024-08-31', user=self.user
        )
        url = '/api/tasks/'  # Direct URL for creating and listing tasks
        response = self.client.get(url, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_task(self):
        task = Task.objects.create(
            title='Task 1', description='Test task', status='pending', due_date='2024-08-31', user=self.user
        )
        url = f'/api/tasks/{task.id}/'  # Direct URL for retrieving a specific task
        response = self.client.get(url, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_update_task(self):
        task = Task.objects.create(
            title='Task 1', description='Test task', status='pending', due_date='2024-08-31', user=self.user
        )
        url = f'/api/tasks/{task.id}/'  # Direct URL for updating a specific task
        data = {
            'title': 'Updated Task 1', 
            'description': 'Updated description', 
            'status': 'completed', 
            'due_date': '2024-08-31'
        }
        response = self.client.patch(url, data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task 1')
        self.assertEqual(task.status, 'completed')

    def test_delete_task(self):
        task = Task.objects.create(
            title='Task 1', description='Test task', status='pending', due_date='2024-08-31', user=self.user
        )
        url = f'/api/tasks/{task.id}/'  # Direct URL for deleting a specific task
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
