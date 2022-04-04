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
        user = kwargs.get('user')
        self.user = user
        #TODO The next lines of code has to be changed 
        # when multiple compnay is allowed
        user_company = Company.objects.filter(created_by=user).first()
        super(BrandForm, self).__init__(*args, **kwargs)
        self.initial['company'] = user_company
