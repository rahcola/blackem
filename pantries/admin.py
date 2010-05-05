from blackem.pantries.models import Pantry, Content
from django.contrib import admin

class PantryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'pantry')
    list_filter = ('pantry',)

admin.site.register(Pantry, PantryAdmin)
admin.site.register(Content, ContentAdmin)

