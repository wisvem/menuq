from django.db import models

from apps.companies.models.brand import Brand


class TimeStampMixin(models.Model):
    """Abstract class for time stamp
    """
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class BasicInfoMixin(models.Model):
    """Abstract class for basic info
    """
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=10000,
        null=True,
        blank=True
    )
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True
