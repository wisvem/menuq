from apps.base.models.mixins import *


class Category(BasicInfoMixin, TimeStampMixin):
    parent_id = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    category_id = models.BigAutoField(
        primary_key=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent_id', 'category_id'],
                name='unique_category'
            )
        ]
