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
    
    def __init__(self, *args, **kwargs):
        super(MenuDetailForm, self).__init__(*args, **kwargs)
        print(kwargs)


MenuDetailFormset = inlineformset_factory(
    Menu,
    MenuDetail,
    form=MenuDetailForm
)
