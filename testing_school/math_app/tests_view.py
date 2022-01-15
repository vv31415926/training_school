from django.test import TestCase
from django.test import Client
from user_app.models import *
from math_app.models import *
from faker import Faker

class OpenViewTest( TestCase ):
    def setUp(self):
        faker = Faker(['ru_Ru'])
        self.client = Client()

        part1 = Partition.objects.create(num=1, name=faker.text())
        theme1 = Theme.objects.create( num=1, name=faker.text(), partition_id=part1.id)
        task = Task.objects.create( numtask=1, variant=1, numclass=10, theme_id=theme1.pk )
        #print('>>>>> task:', Task.objects.all().count())

        user1 = MathUser.objects.create_user(username='testuser1', email='testuser1@mail.ru', password='1234567890')
        user2 = MathUser.objects.create_superuser(username='testuser2', email='testuser2@mail.ru', password='1234567890')

    def test_statuses(self):
        response = self.client.get( '/' )
        self.assertEqual( response.status_code, 200 )

        response = self.client.get('/newversion/1/')
        self.assertEqual(response.status_code, 200)

    def test_none(self):
        response = self.client.get( '/31415926' )
        self.assertEqual( response.status_code, 404 )

        response = self.client.get('/newversion/')
        self.assertEqual(response.status_code, 404)

    def test_login_user(self):
        # нет вошедшего пользователя - нельзя
        response = self.client.get('/table_tasks/')
        self.assertEqual(response.status_code, 302)

        # вошел обычный пользователь - нельзя
        self.client.login(username='testuser1', email='testuser1@mail.ru', password='1234567890')
        response = self.client.get('/table_tasks/')
        self.assertEqual(response.status_code, 403)
        #self.client.logout()

        # вошел супер пользователь - можно
        self.client.login(username='testuser2', email='testuser2@mail.ru', password='1234567890')
        response = self.client.get('/table_tasks/')
        self.assertEqual(response.status_code, 200)

    def test_logout_required(self):
        response = self.client.get('/users/logout/')
        self.assertEqual(response.status_code, 302)

    def test_login_required(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)