"""Price lists Serializer view"""

from apps.api.serializers.price_list import PriceListSerializer
from apps.products.models.price_list import PriceList
from rest_framework import viewsets


class PriceListViewSet(viewsets.GenericViewSet):
    """
    API endpoint to allow price lists to be viewed or edited
    """
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer
