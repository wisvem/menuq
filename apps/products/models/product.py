from apps.base.models.mixins import *
from apps.products.models.category import Category


class Product(BasicInfoMixin, TimeStampMixin):
    photo = models.ImageField(null=True)
