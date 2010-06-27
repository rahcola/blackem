from django.db import models
from django import forms
from blackem.pantries.models import Pantry
from blackem.products.models import Product

class Shoppinglist(models.Model):
    name = models.CharField(max_length=100)
    pantry = models.ForeignKey(Pantry)

    def __unicode__(self):
        return unicode(self.name)

class ShoppinglistForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('my_user', False)
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['pantry'].empty_label = None
        if user:
            self.fields['pantry'].queryset = Pantry.objects.filter(owner=user)

    class Meta:
        model = Shoppinglist

class Item(models.Model):
    shoppinglist = models.ForeignKey(Shoppinglist)
    product = models.ForeignKey(Product)
    amount = models.FloatField()
    bought = models.BooleanField()

    def __unicode__(self):
        return u"{0} {1} of {2} in {3}".format(self.amount, self.product.unit, self.product, self.shoppinglist)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('amount',)

