from django.db import models


# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=25)
    Discription = models.TextField(null=False)
    item_cost = models.IntegerField()
    stock_quantity = models.IntegerField()
    volume = models.PositiveIntegerField(blank=True,null=False)

class Meta:
    Product = ['Name', 'item_cost', 'stock_quantity', 'volume']