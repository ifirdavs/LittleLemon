from django.test import TestCase
from restaurant.models import *

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=0.99, inventory=100)
        self.assertEqual(item.title, 'IceCream')
        self.assertEqual(item.price, 0.99)
        self.assertEqual(item.inventory, 100)
