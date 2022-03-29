from moneyed import CURRENCIES

from apps.base.models.mixins import *
from apps.companies.models.brand import Brand


class Menu(BasicInfoMixin, TimeStampMixin):
    currency = models.CharField(
        max_length=3,
        choices=[(key, key) for key in CURRENCIES]
    )
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE,
        related_name='menus'
    )
    is_Active = models.BooleanField(default=False)

    def __str__(self):
        return(f'{self.name} {self.brand}')
