"""Price Serializer view"""

from apps.api.serializers.product_price import ProductPriceSerializer
from apps.products.models.product_price import ProductPrice
from rest_framework.viewsets import ModelViewSet


class ProductPriceViewSet(ModelViewSet):
    """
    API endpoint to allow prices to be viewed or edited
    """
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
