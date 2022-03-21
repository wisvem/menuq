from moneyed import CURRENCIES

from apps.base.models.mixins import *


class Menu(BasicInfoMixin, TimeStampMixin):
    currency = models.CharField(
        max_length=3,
        choices=[(key, key) for key in CURRENCIES]
    )
    qr_code = models.ImageField(null=True)
