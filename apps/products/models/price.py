from django.db import models
from .product import Product
from .price_list import PriceList


class Price(models.Model):
    product = models.ForeignKey(
        Product,
        null=False,
        on_delete=models.CASCADE
    )
    price_list = models.ForeignKey(
        PriceList, null=False,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0,
        null=False
    )
