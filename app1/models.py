from django.db import models

# Create your models here.

class new_users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)




class Event(models.Model):
    ename = models.CharField(max_length=20)
    eprice = models.CharField(max_length=100)

class details(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    startdate = models.DateField(max_length=100, default='')
    enddate = models.DateField(max_length=100, default='')
    food = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    light = models.CharField(max_length=100)
    flower = models.CharField(max_length=100)
    seet = models.CharField(max_length=100)
    equpment = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
