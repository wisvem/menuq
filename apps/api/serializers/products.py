from apps.products import models
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntergerField(
        read_only=True
    )
    name = serializers.CharField(
        required=True,
        allow_blank=False,
    )
