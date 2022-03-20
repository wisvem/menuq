"""Category Serializer view"""

from apps.api.serializers.category import CategorySerializer
from apps.products.models.category import Category
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    """
    API endpoint to allow categories to be viewed or edited
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
