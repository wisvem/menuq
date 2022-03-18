from django.db import models
from moneyed import list_all_currencies


class PriceList(model.Model):
    name = models.CharField(
        max_length=100
    )
    currency = models.CharField(
        max_length=3,
        choices=list_all_currencies()
    )
    created = models.DateTimeField(auto_now_add=True)
