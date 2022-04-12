from django.urls import reverse

from moneyed import CURRENCIES

from apps.base.models.mixins import *
from apps.companies.models.brand import Brand


class Menu(BasicInfoMixin, TimeStampMixin):
    CURRENCY_CHOICES = [(None, 'Select currency')] 
    CURRENCY_CHOICES += [(key, key) for key in CURRENCIES]
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES
    )
    brand = models.ForeignKey(
        Brand,
        null=False,
        on_delete=models.CASCADE,
        related_name='menus'
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return(f'{self.name} {self.brand}')

    def get_absolute_url(self):
        return reverse(
            "menu_detail", kwargs={
                "brand_id": self.brand_id,
                "menu_id": self.id
            }
        )
    