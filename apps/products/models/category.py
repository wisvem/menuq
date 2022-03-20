from apps.base.models.mixins import *
from mptt.models import MPTTModel, TreeForeignKey


class Category(BasicInfoMixin, TimeStampMixin, MPTTModel):
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
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
