from apps.base.models.mixins import *
from django.db import models

from .category import Category
from .product import Product


class ProductCategory(BasicInfoMixin, TimeStampMixin):
    category_id = models.ForeignKey(
        Category,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['category_id', 'product_id'],
                name='unique_product_per_category'
            )
        ]
