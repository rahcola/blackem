from django.db import models
from blackem.pantries.models import Pantry
from blackem.products.models import Product

class Shoppinglist(models.Model):
  name = models.CharField(max_length=100)
  pantry = models.ForeignKey(Pantry)

class Item(models.Model):
  shoppinglist = models.ForeignKey(Shoppinglist)
  product = models.ForeignKey(Product)
  amount = models.FloatField()
  bought = models.BooleanField()
