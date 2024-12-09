from django.db import models

# Create your models here.


class Pizza(models.Model) : 
  Nom = models.CharField(max_length=100)
  Price = models.FloatField(default=0)
  Ingredients = models.CharField(max_length=400)
  Vegetarian = models.BooleanField(default=False)
  
  def __str__(self):
    return self.Nom