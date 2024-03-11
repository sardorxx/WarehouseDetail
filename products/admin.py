from django.contrib import admin
from products.models import Product, Warehouse, ProductMaterial

# Register your models here.

admin.site.register(ProductMaterial)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'product_quantity')


admin.site.register(Product, ProductAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_id', 'material', 'remainder', 'price',)


admin.site.register(Warehouse, WarehouseAdmin)
