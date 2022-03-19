from apps.base.models.mixins import *
from django.db import models

from .price_list import PriceList
from .product import Product


class Price(TimeStampMixin):
    price_list = models.ForeignKey(
        PriceList, null=False,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        null=False,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0,
        null=False
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['price_list', 'product'],
                name='unique_product_per_list'
            )
        ]
