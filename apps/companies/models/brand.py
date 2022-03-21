from .company import Company
from apps.base.models.mixins import *


class Brand(models.Model):
    name = models.CharField(max_length=1000)
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
