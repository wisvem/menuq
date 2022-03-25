#rom mptt.models import MPTTModel, TreeForeignKey

from apps.base.models.mixins import *
from apps.companies.models.brand import Brand


class Category(BasicInfoMixin, TimeStampMixin):
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    def __str__(self):
        return(f'{self.name}')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent', 'name'],
                name='unique_category'
            )
        ]
