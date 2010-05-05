from blackem.products.models import Product, Manufacturer, Category
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'category')
    list_filter = ['category', 'manufacturer']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Manufacturer)

