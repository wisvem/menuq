from apps.base.models.mixins import *
from apps.companies.models.brand import Brand


class Product(BasicInfoMixin, TimeStampMixin):
    photo = models.ImageField(null=True)
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE
    )
