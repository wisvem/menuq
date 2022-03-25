from apps.api.models.mixins import *

from apps.products.models.menu_detail import MenuDetail


class MenuDetailSerializer(ModelSerializer):
    class Meta:
        model = MenuDetail
        fields = (
            'menu',
            'category',
            'product',
            'price',
            'created',
            'updated',
        )
