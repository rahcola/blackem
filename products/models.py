from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey('Manufacturer')
    category = models.ForeignKey('Category',
                                  db_column='category_name')
    unit = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.name)

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = "Categories"

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.name)

