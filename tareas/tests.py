from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json

from django.contrib.auth.models import User
from tareas.factories import TareaFactory


class UserTestCase(TestCase):

    def _login(self):
        self.client = APIClient()
        response = self.client.post(
            '/api/authentication/login/',
            {
                'username': 'testing_login',
                'email': 'testing@testing.com',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {result['key']}")

    def setUp(self):
        user = User(
            email='testing@testing.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()
        self.tarea1 = TareaFactory()
        self.tarea2 = TareaFactory()

    def test_signup_user(self):
        """Check if we can create an user"""
        client = APIClient()
        response = client.post(
            '/api/registration/',
            {
                'email': 'testing1@testing.com',
                'password1': 'rc{4@qHjR>!b`yAV',
                'password2': 'rc{4@qHjR>!b`yAV',
                'username': 'testing'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # get token login
        token_dict = json.loads(response.content)
        client.credentials(HTTP_AUTHORIZATION=f"Token {token_dict['key']}")
        # get data user with token
        user_data_response = client.get(
            '/api/authentication/user/'
        )
        user_data = json.loads(user_data_response.content)
        self.assertEqual(user_data['username'], 'testing')
        self.assertEqual(user_data['email'], 'testing1@testing.com')

    def test_login_user(self):
        """
        Check login with existing user
        """
        client = APIClient()
        response = client.post(
            '/api/authentication/login/',
            {
                'username': 'testing_login',
                'email': 'testing@testing.com',
                'password': 'admin123',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = json.loads(response.content)
        self.assertIn('key', result)

    def test_private_api_tareas(self):
        """
        Check if API is private.
        """
        response = self.client.get('/api/tareas/')
        result = json.loads(response.content)
        self.assertEqual(result['detail'],
                         'Authentication credentials were not provided.')

    def test_get_list_tareas(self):
        """
        Check count tarea object.
        """
        self._login()
        response = self.client.get('/api/tareas/')
        result = json.loads(response.content)
        self.assertEqual(len(result), 2)

        # Add tarea
        TareaFactory()
        response = self.client.get('/api/tareas/')
        result = json.loads(response.content)
        self.assertEqual(len(result), 3)

    def test_modify_tarea(self):
        self._login()
        response = self.client.get('/api/tareas/1/')
        result = json.loads(response.content)
        self.assertEqual(result['completada'], False)

        # modify 'completada'
        response = self.client.put('/api/tareas/1/',
                        {'completada': True,
                         'titulo': result['titulo'],
                         'descripcion': result['descripcion']},
                        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = json.loads(response.content)
        self.assertEqual(result['completada'], True)

    def test_new_tarea(self):
        """
        Add new tarea with API
        """
        self._login()
        response = self.client.get('/api/tareas/')
        result = json.loads(response.content)
        self.assertEqual(len(result), 2)
        response = self.client.post('/api/tareas/',
                                    {
                                        'titulo': 'tarea 3',
                                        'descripcion': 'tarea 3'
                                    })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/api/tareas/')
        result = json.loads(response.content)
        self.assertEqual(len(result), 3)

    def test_delete_tarea(self):
        self._login()
        response = self.client.get('/api/tareas/')
        result = json.loads(response.content)
        self.assertEqual(len(result), 2)
        response = self.client.delete('/api/tareas/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/api/tareas/')
        result = json.loads(response.content)
        self.assertEqual(len(result), 1)
