from blackem.products.models import Product, Category
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

