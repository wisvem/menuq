from mptt.models import MPTTModel, TreeForeignKey

from apps.base.models.mixins import *
from apps.companies.models.brand import Brand


class Category(BasicInfoMixin, TimeStampMixin, MPTTModel):
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent', 'name'],
                name='unique_category'
            )
        ]
