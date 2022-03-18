from apps.products.models.category import Category
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'parent_id',
            'category_id',
            'name',
            'description',
            'created',
            'updated',
        )
