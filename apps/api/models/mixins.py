from apps.products import models
from rest_framework import serializers


class SerialMixin(serializers.Serializer):
    id = serializers.IntergerField(
        read_only=True
    )
    name = serializers.CharField(
        required=True,
        allow_blank=False,
    )
    description = models.TextField(
        required=False,
        allow_blank=True,
        max_length=100
    )
