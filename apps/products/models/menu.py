from apps.base.models.mixins import *
from moneyed import CURRENCIES


class Menu(BasicInfoMixin, TimeStampMixin):
    currency = models.CharField(
        max_length=3,
        choices=[(key, key) for key in CURRENCIES]
    )
