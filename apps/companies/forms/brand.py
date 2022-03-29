from django import forms
from apps.companies.models.brand import *


class BrandForm(forms.ModelForm):
    company = forms.HiddenInput()
    class Meta:
        model = Brand
        fields = {
            'name',
            'description',
            'company'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        self.user = user
        user_company = Company.objects.filter(created_by=user)[0]
        super(BrandForm, self).__init__(*args, **kwargs)
        self.initial['company'] = user_company
