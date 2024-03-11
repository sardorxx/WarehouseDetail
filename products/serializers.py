from rest_framework import serializers
from .models import Warehouse, Product, ProductMaterial


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['warehouse_id', 'material', 'remainder', 'price']


class ProductSerializer(serializers.ModelSerializer):
    material = WarehouseSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'product_quantity', 'material']


class ProductMaterialSerializer(serializers.ModelSerializer):
    result = ProductSerializer(many=True)

    class Meta:
        model = ProductMaterial
        fields = ['result']
