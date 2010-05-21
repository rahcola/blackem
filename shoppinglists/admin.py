from blackem.shoppinglists.models import Shoppinglist, Item
from django.contrib import admin

#class ShoppinglistAdmin(admin.ModelAdmin):

admin.site.register(Shoppinglist)
admin.site.register(Item)

