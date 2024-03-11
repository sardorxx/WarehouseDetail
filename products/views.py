from rest_framework import generics
from .serializers import ProductMaterialSerializer

from .models import ProductMaterial


class ProductListView(generics.ListAPIView):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer
