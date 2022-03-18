from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=10000, null=False, blank=False)
    
