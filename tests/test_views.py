from django.test import TestCase
from restaurant.models import *
from restaurant.serializers import *
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title='Pizza', price=5, inventory=10)
        Menu.objects.create(title='Burger', price=3, inventory=10)

        self.client = APIClient()
        self.token = Token.objects.create(user=User.objects.create(username='admin'))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.data)
