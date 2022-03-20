"""Price lists Serializer view"""

from apps.api.serializers.price_list import PriceListSerializer
from apps.products.models.menu import Menu
from rest_framework.viewsets import ModelViewSet


class PriceListViewSet(ModelViewSet):
    """
    API endpoint to allow price lists to be viewed or edited
    """
    queryset = Menu.objects.all()
    serializer_class = PriceListSerializer
