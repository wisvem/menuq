from django.forms import BaseInlineFormSet, inlineformset_factory

from apps.companies.models import Brand
from apps.menus.models import Category


class CategoryUpdateForm(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(CategoryUpdateForm, self).__init__(*args, **kwargs)
        self.brand = self.instance
        for form in self.forms:
            for field, value in form.fields.items():
                if hasattr(value, 'queryset') and field is not 'id':
                    value.queryset = value.queryset.filter(brand=self.brand)

    class Meta:
        model = Category



CategoryFormSet = inlineformset_factory(
    Brand,
    Category,
    formset=CategoryUpdateForm,
    extra=1,
    fields = [
    'brand',
    'parent',
    'name',
    'description'
    ]
)
