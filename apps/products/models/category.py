from django.db import models


class Category(models.Model):
    parent_id = models.ForeignKey(
        Category, blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    category_id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['parent_id', 'category_id'],
                name='unique_category')
        ]
