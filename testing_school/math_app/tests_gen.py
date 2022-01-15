from django.test import TestCase
from .models import Level
import pandas as pd

class LevelTestCase( TestCase  ):
    def setUp(self):
        data = pd.read_csv('datagen.csv', sep=';')
        for _, row in data.iterrows():
            Level.objects.create( num=row['num'], name=row['text'])

    def test_Level_count(self):
        level = Level.objects.all()
        self.assertEqual( len(level), 10 )





