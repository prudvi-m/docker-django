from django.test import TestCase
from .calc import add

class sampleTest(TestCase):
    
    def test_add_numbers(self):
        self.assertEqual(add(10,11),21)
        
