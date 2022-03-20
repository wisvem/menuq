from apps.base.models.mixins import *

from .category import Category
from .product import Product


class ProductCategory(BasicInfoMixin, TimeStampMixin):
    parent_id = models.ForeignKey(
        Category,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    category_id = models.ForeignKey(
        Category,
        to_fields=['parent_id, category_id'],
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
