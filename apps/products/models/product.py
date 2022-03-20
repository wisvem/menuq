from apps.base.models.mixins import *


class Product(BasicInfoMixin, TimeStampMixin):
    photo = models.ImageField(null=True)
