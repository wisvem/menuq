from apps.products.models.menu import Menu
from rest_framework.serializers import ModelSerializer

class PriceListSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'name',
            'description',
            'currency',
            'created',
            'updated',
        )
