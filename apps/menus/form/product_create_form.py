from django.forms import ModelForm, inlineformset_factory, ImageField, FileInput
from django.forms.widgets import ClearableFileInput

from apps.companies.models import Brand
from apps.menus.models import Product

class MyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = 'Change'
    clear_checkbox_label = 'remove'

class ProductCreateForm(ModelForm):


    class Meta:
        model = Product
        fields = (
            'brand',
            'name',
            'description',
            'photo'
        )


ProductFormSet = inlineformset_factory(
    Brand,
    Product,
    form=ProductCreateForm,
    extra=1
)
