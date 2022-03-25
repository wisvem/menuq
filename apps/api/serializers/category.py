from rest_framework.serializers import ModelSerializer

from apps.menus.models.category import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'parent',
            'id',
            'name',
            'description',
            'brand',
            'created',
            'updated',
        )
