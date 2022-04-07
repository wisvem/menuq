from django import forms
from django.forms.models import inlineformset_factory

from apps.menus.models.menu import Menu
from apps.menus.models.menu_detail import MenuDetail


class MenuDetailForm(forms.ModelForm):
    model = MenuDetail

    class Meta:
        fields = {
            'menu',
            'category',
            'product',
            'price'
        }

MenuDetailFormset = inlineformset_factory(
    Menu,
    MenuDetail,
    fields={
        'menu',
        'category',
        'product',
        'price'
    }
)
