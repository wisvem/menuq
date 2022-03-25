from rest_framework.serializers import PrimaryKeyRelatedField
from apps.api.models.mixins import MixinModelSerializer
from apps.companies.models.company import Company
from apps.companies.models.brand import Brand


class CompanySerializer(MixinModelSerializer):
    brands = PrimaryKeyRelatedField(
        many=True,
        queryset=Brand.objects.all()
    )

    class Meta:
        model = Company
        fields = (
            'company_id',
            'name',
            'country',
            'created',
            'updated',
            'brands'
        )
