# from apps.base.models.mixins import *

# from .category import Category
# from .product import Product


# class ProductCategory(BasicInfoMixin, TimeStampMixin):
#     parent_category = models.ForeignKey(
#         Category,
#         to_field='main_category',
#         blank=True,
#         null=True,
#         on_delete=models.CASCADE,
#         related_name='sub_category'
#     )
#     category = models.ForeignKey(
#         Category,
#         blank=False,
#         null=False,
#         on_delete=models.CASCADE,
#         related_name='category'
#     )
#     product = models.ForeignKey(
#         Product,
#         blank=False,
#         null=False,
#         on_delete=models.CASCADE
#     )

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['parent_category', 'category', 'product'],
#                 name='unique_product_per_category'
#             )
#         ]
