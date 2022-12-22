from django.test import TestCase
from .models import *

class ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        main.objects.create(first_name='test', second_name='123')

    def test_first_name_label(self):
        author=main.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'Логин')
        
    def test_second_name_label(self):
        author=main.objects.get(id=1)
        field_label = author._meta.get_field('second_name').verbose_name
        self.assertEquals(field_label,'Пароль')

    def test_first_name_max_length(self):
        author=main.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,15)
        
    def test_second_name_max_length(self):
        author=main.objects.get(id=1)
        max_length = author._meta.get_field('second_name').max_length
        self.assertEquals(max_length,15)

