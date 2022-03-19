"""Category Serializer view"""

from apps.api.serializers.category import CategorySerializer
from apps.products.models.category import Category
from rest_framework import viewsets


class CategoryViewSet(viewsets.GenericViewSet):
    """
    API endpoint to allow categories to be viewed or edited
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
