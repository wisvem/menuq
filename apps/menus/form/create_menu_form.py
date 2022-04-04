from django.forms import inlineformset_factory
from apps.menus.models.menu_detail import *
from django import forms


class CreateMenuForm(forms.ModelForm):
    brand = forms.HiddenInput()

    class Meta:
        model = Menu
        fields = {
            'brand',
            'name',
            'currency',
            'is_active',
            'description'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        brand = kwargs.get('current_brand')
        self.user = user
        self.brand = brand
        user_brand = Brand.objects.filter(brand=self.brand)
        super(CreateMenuForm, self).__init__(*args, **kwargs)
        self.initial['brand'] = user_brand


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
