from django.forms import Form, inlineformset_factory

from apps.companies.models import Brand
from apps.menus.models import Product


class ProductCreateForm(Form):
    pass


ProductFormSet = inlineformset_factory(
    Brand,
    Product,
    fields=[
        'brand',
        'name',
        'description',
        'photo'
    ],
    extra=1
)
