"""Brand Serializer view"""

from rest_framework.viewsets import ModelViewSet

from apps.api.serializers.brand import BrandSerializer
from apps.companies.models.brand import Brand


class BrandViewSet(ModelViewSet):
    """
    API endpoint to allow brands to be viewed or edited
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
