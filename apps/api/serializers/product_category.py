from apps.products.models.product_category import ProductCategory
from rest_framework.serializers import ModelSerializer


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'category_id',
            'product_id',
            'created',
            'updated',
        )
