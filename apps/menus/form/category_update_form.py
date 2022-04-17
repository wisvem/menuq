from django.forms import ModelForm, inlineformset_factory

from apps.companies.models import Brand
from apps.menus.models import Category


class CategoryUpdateForm(ModelForm):


    class Meta:
        model = Category
        fields = (
            'brand',
            'parent',
            'name',
            'description'
        )


CategoryFormSet = inlineformset_factory(
    Brand,
    Category,
    form=CategoryUpdateForm,
    extra=1
)
