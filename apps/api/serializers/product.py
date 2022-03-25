from rest_framework.serializers import ModelSerializer

from apps.menus.models.product import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'photo',
            'brand',
            'created',
            'updated',
        )
