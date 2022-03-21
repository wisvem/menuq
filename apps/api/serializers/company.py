from rest_framework.serializers import ModelSerializer
from apps.companies.models.company import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'company_id',
            'name',
            'country',
            'created',
            'updated',
        )
