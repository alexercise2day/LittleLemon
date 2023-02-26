from django.db import models

# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, db_column='booking_id')
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(6)
    bookingdata = models.DateField()
    
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True, db_column='menu_id')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(5)
