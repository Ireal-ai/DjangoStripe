from django.contrib import admin

from item.models import ItemModel


# Register your models here.
@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
