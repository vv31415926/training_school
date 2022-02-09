from django.test import TestCase
from faker import Faker
from mixer.backend.django import mixer
from .models import *
from user_app.models import *

pass

#
# class LevelTestCase( TestCase  ):
#     def setUp(self):
#         self.user1 = MathUser.objects.create_user( username='testuser', email='testuser@mail.ru',password='1234567890' )
#         self.level1 = Level.objects.create( num=1, name='Простой')
#         self.level2 = Level.objects.create( num=2, name='Средний')
#         self.level3 = Level.objects.create( num=3, name='Сложный')
#         self.level4 = Level.objects.create( num=4, name='Супер')
#
#         part1 = Partition.objects.create( num=1, name='Вычисления, преобразования' )
#         part2 = Partition.objects.create( num=2, name='Функции')
#
#         theme1 = Theme.objects.create( num=1, name='Арифметические действия, корень, степень, логарифм', partition_id=part1.id )
#         theme2 = Theme.objects.create( num=2, name='Решение уравнений, их систем', partition_id=part2.pk  )
#
#         task1 = Task.objects.create(  numtask=1, variant=1, numclass=10, level_id=self.level1.id, theme_id=theme1.pk )
#         task2 = Task.objects.create(numtask=2, variant=1, numclass=10, level_id=self.level2.pk, theme_id=theme1.pk )
#
#         vers1 = Version.objects.create( npp=1, answer='(-1;2)', correct=True, task_id=task1.pk  )
#         vers2 = Version.objects.create(npp=2, answer='(6;7)', correct=False, task_id=task1.pk)
#         vers3 = Version.objects.create(npp=3, answer='(5;26)', correct=False, task_id=task1.pk)
#         vers4 = Version.objects.create(npp=1, answer='(-1;2)', correct=True, task_id=task2.pk)
#         vers5 = Version.objects.create(npp=2, answer='(6;7)', correct=False, task_id=task2.pk)
#         vers6 = Version.objects.create(npp=3, answer='(5;26)', correct=False, task_id=task2.pk)
#
#         lesson1 = Lesson.objects.create( task_id=task1.id, student_id=self.user1.id )
#
#     def test_count_tasks(self):
#         self.assertEqual( self.level1.get_count_tasks(), 1)
#
#     def test_count_student(self):
#         self.assertEqual( self.user1.get_count_lessons(), 1)
#
#
#
# class LevelTestCaseFaker(TestCase):
#     def setUp(self):
#         faker = Faker(['ru_Ru'])
#         self.user1 = MathUser.objects.create_user(username='testuser', email='testuser@mail.ru', password='1234567890')
#
#
#         self.level1 = Level.objects.create( num=1, name=faker.text())
#         self.level2 = Level.objects.create( num=2, name=faker.text() )
#         part1 = Partition.objects.create( num=1, name=faker.text())
#         theme1 = Theme.objects.create(num=1, name=faker.text(), partition_id=part1.id)
#         task1 = Task.objects.create(numtask=1, variant=1, numclass=10, level_id=self.level1.id, theme_id=theme1.pk)
#         task2 = Task.objects.create(numtask=2, variant=1, numclass=10, level_id=self.level2.id, theme_id=theme1.pk)
#         lesson1 = Lesson.objects.create(task_id=task1.id, student_id=self.user1.id)
#
#     def test_count_tasks(self):
#         self.assertEqual( self.level1.get_count_tasks(), 1  )
#     def test_count_student(self):
#         self.assertEqual( self.user1.get_count_lessons(), 1)
#
# class LevelTestCaseMixer(TestCase):
#     def setUp(self):
#         self.level1 = mixer.blend( Level )
#         self.level2 = mixer.blend( Level )
#         self.user1 = mixer.blend( MathUser )
#         task1 = mixer.blend( Task )
#
#         lesson1 = Lesson.objects.create(task_id=task1.id, student_id=self.user1.id)
#         task1 = mixer.blend( Task, level_id=self.level1.id , question='Функция y=f(x)  задана своим графиком. Укажите в какой точке графика касательная к нему параллельна оси абсциссов.' )
#
#     def test_count_tasks(self):
#         self.assertEqual( self.level1.get_count_tasks(), 1  )
#     def test_count_student(self):
#         self.assertEqual( self.user1.get_count_lessons(), 1 )