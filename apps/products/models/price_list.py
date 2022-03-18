from apps.base.models.abstract import *
from django.db import models
from moneyed import list_all_currencies


class PriceList(BasicInfoMixin, TimeStampMixin):
    currency = models.CharField(
        max_length=3,
        choices=list_all_currencies()
    )
