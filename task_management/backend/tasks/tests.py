from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Task
from .serializers import TaskSerializer


class TaskModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Task 1',
            description='Test task description',
            status='pending',
            due_date='2024-08-31',
            user=self.user
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Task 1')
        self.assertEqual(self.task.description, 'Test task description')
        self.assertEqual(self.task.status, 'pending')
        self.assertEqual(self.task.due_date, '2024-08-31')
        self.assertEqual(self.task.user, self.user)


    def test_task_str_representation(self):
        self.assertEqual(str(self.task), 'Task 1')

    def test_task_default_status(self):
        task = Task.objects.create(
            title='Task 2',
            description='Another test task',
            due_date='2024-09-01',
            user=self.user
        )
        self.assertEqual(task.status, 'pending')



class TaskSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Task 1',
            description='Test task description',
            status='pending',
            due_date='2024-08-31',
            user=self.user
        )
        self.serializer = TaskSerializer(instance=self.task)

    def test_task_serialization(self):
        data = self.serializer.data
        self.assertEqual(data['title'], 'Task 1')
        self.assertEqual(data['description'], 'Test task description')
        self.assertEqual(data['status'], 'pending')
        self.assertEqual(data['due_date'], '2024-08-31')
        self.assertEqual(data['user'], self.user.id)

    def test_task_deserialization(self):
        data = {
            'title': 'Task 2',
            'description': 'New task description',
            'status': 'completed',
            'due_date': '2024-09-01',
            'user': self.user.id
        }
        serializer = TaskSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        task = serializer.save()
        self.assertEqual(task.title, 'Task 2')
        self.assertEqual(task.description, 'New task description')
        self.assertEqual(task.status, 'completed')
        self.assertEqual(task.due_date.strftime('%Y-%m-%d'), '2024-09-01')
        self.assertEqual(task.user, self.user)

    def test_task_validation(self):
        # Invalid data
        invalid_data = {
            'title': '',
            'description': 'No title task',
            'status': 'completed',
            'due_date': '2024-09-01',
            'user': self.user.id
        }
        serializer = TaskSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), {'title'})



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