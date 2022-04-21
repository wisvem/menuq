from django import forms
from apps.companies.models.brand import *


class BrandForm(forms.ModelForm):
    company = forms.HiddenInput()

    class Meta:
        model = Brand
        fields = {
            'name',
            'photo',
            'description',
            'company'
        }

    def __init__(self, *args, **kwargs):
        try:
            user = kwargs.pop('user')
            self.user = user
            # TODO The next lines of code has to be changed
            # when multiple compnay is allowed
            company = Company.objects.filter(created_by=user).first()
        except:
            company = kwargs.get('instance').company

        super(BrandForm, self).__init__(*args, **kwargs)
        self.initial['company'] = company
