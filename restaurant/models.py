from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    def __str__(self) -> str:
        return f'{self.title}: {str(self.price)}'
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingdate = models.DateField()
    def __str__(self) -> str:
        return self.name

