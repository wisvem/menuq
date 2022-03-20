from django.db import models
from .company import Company


class Brand(models.Model):
    name = models.CharField(max_length=1000)
    company = models.ForeignKey(Company, null=False, blank=False)
