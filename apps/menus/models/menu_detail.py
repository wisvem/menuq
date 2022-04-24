from apps.base.models.mixins import *

from .category import Category
from .menu import Menu
from .product import Product


class MenuDetail(TimeStampMixin):
    menu = models.ForeignKey(
        Menu, null=False,
        on_delete=models.CASCADE,
        related_name='menu_details'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_details'
    )
    product = models.ForeignKey(
        Product,
        null=False,
        on_delete=models.CASCADE,
        related_name='menu_details'
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=0,
        default=0,
        null=False
    )
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return(f'{self.category} {self.product.name} {self.price}')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['menu', 'product'],
                name='unique_product'
            )
        ]
        ordering = ['order']
