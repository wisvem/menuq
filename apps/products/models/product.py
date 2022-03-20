from apps.base.models.mixins import *
from apps.products.models.category import Category


class Product(BasicInfoMixin, TimeStampMixin):
    photo = models.ImageField(null=True)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
