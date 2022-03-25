from .company import Company
from apps.base.models.mixins import *


class Brand(TimeStampMixin):
    name = models.CharField(max_length=1000)
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='brands'
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return(f'{self.name} {self.company}')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'name'],
                name='unique_brand'
            )
        ]
