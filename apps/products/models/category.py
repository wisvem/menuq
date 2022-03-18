from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    super_id = models.ForeignKey(Category, blank=True)
