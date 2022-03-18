from apps.products.models.price_list import PriceList
from rest_framework.serializers import ModelSerializer

class PriceListSerializer(ModelSerializer):
    class Meta:
        model = PriceList
        fields = (
            'name',
            'description',
            'currency',
            'created',
            'updated',
        )
