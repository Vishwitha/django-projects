from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=10)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Customer(models.Model):
    firstname=models.CharField(max_length=256)
    lastname =models.CharField(max_length=256)
    phone=models.PositiveIntegerField()

    def __str__(self):
        return (self.firstname +' '+self.lastname)
