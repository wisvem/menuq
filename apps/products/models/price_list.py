from apps.base.models.mixins import *
from django.db import models
from moneyed import CURRENCIES


class PriceList(BasicInfoMixin, TimeStampMixin):
    currency = models.CharField(
        max_length=3,
        choices=[(key, key) for key in CURRENCIES]
    )
