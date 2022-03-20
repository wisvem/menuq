"""Price Serializer view"""

from apps.api.serializers.price import PriceSerializer
from apps.products.models.price import Price
from rest_framework.viewsets import ModelViewSet


class PriceViewSet(ModelViewSet):
    """
    API endpoint to allow prices to be viewed or edited
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
