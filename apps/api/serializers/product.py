from apps.products.models.product import Product
from rest_framework.serializers import ModelSerializer


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
