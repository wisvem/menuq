from apps.products.models.product_price import Price
from rest_framework.serializers import ModelSerializer


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'price_list',
            'product',
            'price',
            'created',
            'updated',
        )
