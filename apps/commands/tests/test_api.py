from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from population_script import add_user, add_command

from apps.commands.models import Command
User = get_user_model()


def create_client(data, url, get=True, kwargs=None):
    client = APIClient()
    client.login(username=data['username'],
                 password=data['password'])
    if get:
        return client.get(url, kwargs=kwargs or None)
    return client.post(url, data=kwargs or None)


class TestUserAPI(APITestCase):
    def setUp(self):
        self.user_data = {'username': 'username', 'password': 'password',
                          'first_name': 'first', 'last_name': 'last',
                          'email': 'email@email.com'}
        add_user(**self.user_data)

    def test_GET_user(self):
        response = create_client(self.user_data, reverse('user-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)

    def test_GET_user_detail(self):
        response = create_client(
            self.user_data,
            reverse('user-detail', kwargs={'pk': User.objects.first().pk}))

        updated_dict = {'pk': User.objects.first().pk}
        updated_dict.update(self.user_data)
        del updated_dict['password']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data), updated_dict)

    def test_POST_user_list(self):
        temp = {'username': 'use', 'password': 'pass', 'email': 'e@email.com'}
        response = create_client(
            self.user_data,
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


class TestCommandAPI(APITestCase):
    def setUp(self):
        self.data = {'username': 'username', 'password': 'password',
                     'first_name': 'first', 'last_name': 'last',
                     'email': 'email@email.com'}
        user = add_user(**self.data)
        self.c_data = {'command': 'ls -al', 'user': user,
                       'note': '', 'os': '', 'version': ''}
        self.command = add_command(**self.c_data)

    def test_GET_command_list(self):
        response = create_client(self.data, reverse('commands-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Command.objects.count())

    def test_GET_command_detail(self):
        response = create_client(
            self.data,
            reverse('commands-detail', kwargs={'pk': self.command.pk}))
        temp = {'id': self.command.pk}
        temp.update(self.c_data)
        temp['user'] = temp['user'].pk

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, temp)

    def test_POST_command_list(self):
        data = {'command': 'command', 'os': 'L', 'note': 'note',
                'version': '1', 'user': self.c_data['user'].pk}
        response = create_client(self.data, reverse('commands-list'),
                                 get=False, kwargs=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictContainsSubset(data, response.data)

    def test_POST_command_detail(self):
        data = {'os': 'W'}
        client = APIClient()
        client.login(username=self.data['username'],
                     password=self.data['password'])
        response = client.patch(
            reverse('commands-detail', kwargs={'pk': self.command.pk}),
            data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['os'], data['os'])
        self.assertNotEqual(self.command.os, data['os'])
