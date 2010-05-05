from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey('Manufacturer',
                                      db_column='manufacturer_name')
    category = models.ForeignKey('Category',
                                  db_column='category_name')
    unit = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

