from apps.base.models.mixins import *
from django_countries.fields import CountryField


class Company(BasicInfoMixin, TimeStampMixin):
    company_id = models.CharField(max_length=20)
    country = CountryField(blank_label='(select country)')

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company_id', 'country'],
                name='unique_company'
            )
        ]
