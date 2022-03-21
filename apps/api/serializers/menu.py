from rest_framework.serializers import ModelSerializer

from apps.products.models.menu import Menu


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'name',
            'description',
            'currency',
            'brand',
            'created',
            'updated',
        )
