from .company import Company
from apps.base.models.mixins import *

class Brand(BasicInfoMixin, TimeStampMixin):
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='brands'
    )
    qr_code = models.ImageField(null=True, upload_to='qrcodes', blank=True)

    def __str__(self):
        return(f'{self.name}')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'name'],
                name='unique_brand'
            )
        ]
