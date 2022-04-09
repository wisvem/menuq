from django import forms
from django.forms import BaseInlineFormSet, inlineformset_factory

from apps.menus.models.menu import Menu
from apps.menus.models.menu_detail import MenuDetail


class MenuDetailForm(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(MenuDetailForm, self).__init__(*args, **kwargs)
        self.brand = self.instance.brand
        for form in self.forms:
            for field, value in form.fields.items():
                if hasattr(value, 'queryset') and field is not 'id':
                    value.queryset = value.queryset.filter(brand=self.brand)


MenuDetailFormset = inlineformset_factory(
    Menu,
    MenuDetail,
    fields=[
        'menu',
        'category',
        'product',
        'price'
    ],
    formset=MenuDetailForm,
    extra=1
)
