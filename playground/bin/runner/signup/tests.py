from django.test import TestCase, Client

from django.contrib.auth.models import User


class LoginTests(TestCase):
    '''
    test class that will test actions about user object handling
    '''
    def test_create_user(self):
        user = User.objects.create_user('test_user', 'yonchoy@abv.bg', 'pass')
        user.save()

    def test_error_login(self):
        client = Client()
        response = client.post('/login/', {'username': 'test_user', 'password': 'zxc'})
        self.assertEqual(response.status_code, 401)

    def test_logout(self):
        client = Client()
        response = client.get('/logout/', follow=True)
        self.assertEqual(response.status_code, 200)

