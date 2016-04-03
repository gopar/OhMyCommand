from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from population_script import populate, add_user, add_command

User = get_user_model()


class TestUserAPI(APITestCase):
    def setUp(self):
        self.user_data = {'username': 'username', 'password': 'password',
                          'first_name': 'first', 'last_name': 'last',
                          'email': 'email@email.com'}
        add_user(**self.user_data)

    def create_client(self, url, get=True, kwargs=None):
        client = APIClient()
        client.login(username=self.user_data['username'],
                     password=self.user_data['password'])
        if get:
            return client.get(url, kwargs=kwargs or None)
        return client.post(url, data=kwargs or None)

    def test_GET_user(self):
        response = self.create_client(reverse('user-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)

    def test_GET_user_detail(self):
        response = self.create_client(
            reverse('user-detail', kwargs={'pk': User.objects.first().pk}))

        updated_dict = {'pk': User.objects.first().pk}
        updated_dict.update(self.user_data)
        del updated_dict['password']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data), updated_dict)

    def test_POST_user_list(self):
        temp = {'username': 'use', 'password': 'pass', 'email': 'e@email.com'}
        response = self.create_client(
            reverse('user-list'), get=False, kwargs=temp)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        # TODO: Test when we get token keys

    def test_POST_user_detail(self):
        client = APIClient()
        client.login(username=self.user_data['username'],
                     password=self.user_data['password'])

        name = self.user_data['first_name']
        user = User.objects.filter(first_name=name)[0]
        temp = {'first_name': 'test', 'email': user.email}

        # TODO: Figure out why we need to pass 'email' to make patch request
        response = client.patch(reverse('user-detail', kwargs={'pk': user.pk}),
                                data=temp)

        self.assertNotEqual(user.first_name, response.data['first_name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp['first_name'], response.data['first_name'])
