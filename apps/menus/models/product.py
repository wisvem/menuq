from apps.base.models.mixins import *
from apps.companies.models.brand import Brand
from apps.base.helpers import custom_path
from django.core.validators import validate_image_file_extension
import os


class Product(BasicInfoMixin, TimeStampMixin):
    photo = models.ImageField(
        upload_to=custom_path,
        null=True,
        blank=True,
        validators=[validate_image_file_extension]
    )
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return(f'{self.name}')
