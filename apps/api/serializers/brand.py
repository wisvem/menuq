from rest_framework.serializers import ModelSerializer
from apps.companies.models.brand import Brand


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'name',
            'company',
            'created',
            'updated',
        )
