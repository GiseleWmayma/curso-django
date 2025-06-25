from django.test import TestCase
from django.urls import reverse

class RecipeURLsTest(TestCase):   
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home') #o que eu to testando
        self.assertEqual(home_url, '/') #se url é igual a barra
        
