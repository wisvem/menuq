from apps.base.models.mixins import *

from .category import Category
from .menu import Menu
from .product import Product


class MenuDetail(TimeStampMixin):
    menu = models.ForeignKey(
        Menu, null=False,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
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
                fields=['menu', 'product', 'brand'],
                name='unique_product_per_list'
            )
        ]