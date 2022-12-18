from django.db import models

# Create your models here.
class users(models.Model):
    fullname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)


class Item(models.Model):
    name = models.CharField(max_length=50)
    rate = models.IntegerField()
    photo = models.FileField()
 

