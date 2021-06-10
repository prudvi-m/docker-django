from django.test import TestCase
from .calc import add,subtract

class sampleTest(TestCase):
    
    
    def test_add_numbers(self):
        
        self.assertEqual(add(10,11), 21)
        
    def test_subtract_numbers(self):
        self.assertEqual(subtract(20,10),10)
        
