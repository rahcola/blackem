from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from blackem.products.models import Product

class Pantry(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pantries"

class PantryForm(ModelForm):
    class Meta:
        model = Pantry
        fields = ('name',)

class Content(models.Model):
    pantry = models.ForeignKey(Pantry)
    product = models.ForeignKey(Product)
    amount = models.FloatField()

    def __unicode__(self):
        return unicode("{0} {1} {2}".format(self.product.name,
                                           self.amount,
                                           self.product.unit))

