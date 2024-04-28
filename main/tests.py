from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from .views import UserView

class UserViewTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='adminpassword')

    def test_create_user(self):
        factory = APIRequestFactory()
        view = UserView.as_view()
        request = factory.post('user/create/', {'username': 'testuser', 'password': 'testpassword', 'first_name': 'Test'})
        force_authenticate(request, user=self.admin_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_create_user_existing_username(self):
        factory = APIRequestFactory()
        view = UserView.as_view()
        request = factory.post('/user/create/', {'username': 'admin', 'password': 'testpassword', 'first_name': 'Test'})
        force_authenticate(request, user=self.admin_user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['status'], 'The username already exist')


from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import cd_file

class TestFileUploadAndDelete(TestCase):
    def test_file_upload(self):
        factory = APIRequestFactory()
        file_data = {
            'file': open('12.docx', 'rb'),  
            'description': 'Test description'
        }
        request = factory.post('/add/file/', file_data, format='multipart')
        response = cd_file(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], True)

    def test_file_delete(self):
        factory = APIRequestFactory()
        file_data = {
            'id': 1  
        }
        request = factory.delete('/delete/file/', file_data, format='json')
        response = cd_file(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], True)
