"""Company Serializer view"""

from rest_framework.viewsets import ModelViewSet

from apps.api.serializers.company import CompanySerializer
from apps.companies.models.company import Company


class CompanyViewSet(ModelViewSet):
    """
    API endpoint to allow companies to be viewed or edited
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
