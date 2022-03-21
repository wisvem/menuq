"""Product Serializer view"""

from rest_framework.viewsets import ModelViewSet

from apps.api.serializers.product import ProductSerializer
from apps.products.models.product import Product


class ProductViewSet(ModelViewSet):
    """
    API endpoint to allow products to be viewed or edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
