from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from blackem.products.models import Product

class Pantry(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.name)
    
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
       return u"{0} {1} of {2} in {3}".format(self.amount, self.product.unit,
                                              self.product, self.pantry) 

class ContentForm(ModelForm):
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise ValidationError("No negative amounts.")
        return amount

    class Meta:
        model = Content
        fields = ('amount',)
