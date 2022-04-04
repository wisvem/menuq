from django import forms
from apps.companies.models.company import *


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = {
            'company_id',
            'name',
            'description',
            'country'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        self.user = user
        super(CompanyForm, self).__init__(*args, **kwargs)
