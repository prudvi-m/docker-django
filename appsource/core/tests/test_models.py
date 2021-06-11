from django.test import TestCase
from django.contrib.auth import get_user_model

class test_models(TestCase):
    
    
    def test_user_creation(self):
        """ Tests user creation up on successful email """
        email = 'prudvi@ok.com'
        password = 'abcd1234'
        
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEqual(email,user.email)
        self.assertTrue(user.check_password(password))
        
        
        