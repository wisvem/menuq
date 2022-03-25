from apps.menus.models.menu_detail import MenuDetail
from apps.menus.models.menu import Menu
from rest_framework.serializers import PrimaryKeyRelatedField
from apps.api.models.mixins import MixinModelSerializer


class MenuSerializer(MixinModelSerializer):
    menu_details = PrimaryKeyRelatedField(
        many=True,
        queryset=MenuDetail.objects.all()
    )
    class Meta:
        model = Menu
        fields = (
            'name',
            'description',
            'currency',
            'brand',
            'created',
            'updated',
            'menu_details'
        )
