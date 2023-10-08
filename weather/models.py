from django.db import models

# Create your models here.

class Weather(models.Model):
    nameLocal = models.CharField(max_length=255)
    favorite = models.BooleanField()


