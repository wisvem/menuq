"""Price lists Serializer view"""

from rest_framework.viewsets import ModelViewSet

from apps.api.serializers.menu import MenuSerializer
from apps.menus.models.menu import Menu


class MenuViewSet(ModelViewSet):
    """
    API endpoint to allow price lists to be viewed or edited
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
