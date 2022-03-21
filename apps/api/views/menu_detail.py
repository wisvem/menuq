"""Price Serializer view"""

from rest_framework.viewsets import ModelViewSet

from apps.api.serializers.menu_detail import MenuDetailSerializer
from apps.products.models.menu_detail import MenuDetail


class MenuDetailViewSet(ModelViewSet):
    """
    API endpoint to allow prices to be viewed or edited
    """
    queryset = MenuDetail.objects.all()
    serializer_class = MenuDetailSerializer
