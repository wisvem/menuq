from apps.base.models.mixins import *
from django.db import models


class Product(BasicInfoMixin, TimeStampMixin):
    photo = models.ImageField(null=True)
