from apps.products.models.product_price import ProductPrice
from rest_framework.serializers import ModelSerializer


class ProductPriceSerializer(ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = (
            'price_list',
            'product',
            'price',
            'created',
            'updated',
        )
