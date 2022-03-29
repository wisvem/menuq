from .company import Company
from apps.base.models.mixins import *


class Brand(BasicInfoMixin, TimeStampMixin):
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='brands'
    )
    qr_code = models.ImageField(null=True)

    def __str__(self):
        return(f'{self.name}')

    # def save(self, *args, **kwargs):
    #     if self.company is None:
    #         self.company = Company.objects.filter(created_by=request.user)[0]
    #     super(Brand, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['company', 'name'],
                name='unique_brand'
            )
        ]
