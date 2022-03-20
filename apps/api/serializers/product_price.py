from apps.products.models.menu_detail import MenuDetail
from rest_framework.serializers import ModelSerializer


class ProductPriceSerializer(ModelSerializer):
    class Meta:
        model = MenuDetail
        fields = (
            'menu',
            'product',
            'price',
            'created',
            'updated',
        )
