from apps.base.models.mixins import *

from .category import Category
from .product import Product


class ProductCategory(BasicInfoMixin, TimeStampMixin):
    parent_category = models.ForeignKey(
        Category,
        to_field='parent_id',
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        to_field='category_id',
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent_category', 'category', 'product'],
                name='unique_product_per_category'
            )
        ]
