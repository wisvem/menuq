"""Price Serializer view"""

from apps.api.serializers.product_price import ProductPriceSerializer
from apps.products.models.menu_detail import MenuDetail
from rest_framework.viewsets import ModelViewSet


class ProductPriceViewSet(ModelViewSet):
    """
    API endpoint to allow prices to be viewed or edited
    """
    queryset = MenuDetail.objects.all()
    serializer_class = ProductPriceSerializer
