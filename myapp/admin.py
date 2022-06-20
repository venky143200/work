from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name', 'item_cost', 'stock_quantity', 'volume']


admin.site.register(Product)