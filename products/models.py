from django.db import models


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(null=True, blank=True)
    material = models.CharField(max_length=255)
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    product_quantity = models.IntegerField()
    material = models.ManyToManyField(Warehouse)


class ProductMaterial(models.Model):
    result = models.ManyToManyField(Product)
