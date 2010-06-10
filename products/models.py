from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    categories = models.ManyToManyField('Category')
    unit = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.name)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = "Categories"

