"""Product Serializer view"""

from apps.api.serializers.product import ProductSerializer
from apps.products.models.product import Product
from rest_framework import viewsets


class ProductViewSet(viewsets.GenericViewSet):
    """
    API endpoint to allow products to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
