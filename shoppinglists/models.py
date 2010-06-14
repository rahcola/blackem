from django.db import models
from django.forms import ModelForm, ModelChoiceField, CharField
from blackem.pantries.models import Pantry
from blackem.products.models import Product

class Shoppinglist(models.Model):
    name = models.CharField(max_length=100)
    pantry = models.ForeignKey(Pantry)

    def __unicode__(self):
        return unicode(self.name)

class ShoppinglistForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('my_user', False)
        ModelForm.__init__(self, *args, **kwargs)
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

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('amount',)
