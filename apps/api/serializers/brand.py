from rest_framework.serializers import PrimaryKeyRelatedField
from apps.companies.models.brand import Brand
from apps.menus.models.menu import Menu
from apps.api.models.mixins import *


class BrandSerializer(ModelSerializer):
    menus = PrimaryKeyRelatedField(
        many=True,
        queryset=Menu.objects.all()
    )

    class Meta:
        model = Brand
        fields = (
            'name',
            'company',
            'created',
            'updated',
            'menus'
        )
