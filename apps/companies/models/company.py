from django.db import models


class Company(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=1000)
