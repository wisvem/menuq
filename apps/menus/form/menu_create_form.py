from django.forms import inlineformset_factory
from apps.menus.models.menu_detail import *
from django import forms
from apps.companies.models.brand import Brand
from django.http import Http404


class MenuCreateForm(forms.ModelForm):
    brand = forms.HiddenInput()

    class Meta:
        model = Menu
        fields = {
            'name',
            'currency',
            'is_active',
            'description',
            'brand',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        brand = kwargs.pop('brand')
        self.user = user
        self.brand = brand
        brand = Brand.objects.get(pk=self.brand, created_by=self.user)
        if not brand:
            raise Http404()
        super(MenuCreateForm, self).__init__(*args, **kwargs)
        self.initial['brand'] = brand
