from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.forms import inlineformset_factory

from django.http import Http404
from apps.companies.models.brand import Brand
from apps.menus.models.menu_detail import *


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
        try:
            brand = Brand.objects.get(pk=self.brand, created_by=self.user)
            super(MenuCreateForm, self).__init__(*args, **kwargs)
            self.initial['brand'] = brand
        except ObjectDoesNotExist:
            pass
