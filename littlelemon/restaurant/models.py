from django.db import models

# Create your models here.
class Booking(models.Model):
    bid = models.IntegerField(blank=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(blank=True)
    bookingdata = models.DateField()
    
class Menu(models.Model):
    mid = models.IntegerField(blank=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(blank=True)
