from django.db import models


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

    class Meta:
        abstract = True
