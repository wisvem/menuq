from .company import Company
from apps.base.models.mixins import *
from apps.base.helpers import custom_path
from django.core.validators import validate_image_file_extension


class Brand(BasicInfoMixin, TimeStampMixin):
    photo = models.ImageField(
        upload_to=custom_path,
        null=True,
        blank=True,
        validators=[validate_image_file_extension]
    )
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='brands'
    )
    qr_code = models.ImageField(
        upload_to='qrcodes/',
        null=True,
        blank=True
    )

    def __str__(self):
        return(f'{self.name}')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'name'],
                name='unique_brand'
            )
        ]
