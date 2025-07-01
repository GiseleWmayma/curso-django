from django.test import TestCase
from django.urls import reverse
class RecipeURLsTest(TestCase):   
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home') #o que eu to testando
        self.assertEqual(home_url, '/') #se url é igual a barra
        
    def test_recipe_category_url_is_correct(self):
        home_url = reverse('recipes:category', kwargs={'category_id': 1}) #testando com argumentos: em ordem> args=(1,),kwargs= manda um dicionario
        self.assertEqual(home_url, '/recipes/category/1/') #se url é igual a barra
        
    def test_recipe_detail_url_is_correct(self):
        home_url = reverse('recipes:recipe', kwargs={'id': 1}) #testando com argumentos: em ordem> args=(1,),kwargs= manda um dicionario
        self.assertEqual(home_url, '/recipes/1/') #se url é igual a barra
