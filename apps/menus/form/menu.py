from django.forms import inlineformset_factory
from apps.menus.models.menu_detail import *
from django import forms


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = {
            'brand',
            'name',
            'currency'
            'description',
            'is_active'
        }


class MenuDetailForm(forms.ModelForm):
    model = MenuDetail

    class Meta:
        fields = {
            'menu',
            'category',
            'product',
            'price'
        }


MenuDetailInlineFormset = inlineformset_factory(
    Menu,
    MenuDetail,
    form=MenuDetailForm,
    extra=5,
)
