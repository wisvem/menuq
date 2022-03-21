from apps.base.models.mixins import *
from django_countries.fields import CountryField


class Company(TimeStampMixin):
    company_id = models.CharField(max_length=20)
    name = models.CharField(max_length=1000)
    country = CountryField(blank_label='(select country)')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company_id', 'country'],
                name='unique_company'
            )
        ]
