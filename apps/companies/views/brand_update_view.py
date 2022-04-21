from django.views.generic import ListView, UpdateView

from apps.companies.models.brand import Brand
from apps.base.models.mixins import OwnerMixin
from apps.companies.forms import BrandForm
from django.views.generic.edit import DeletionMixin


class BrandUpdateView(UpdateView, OwnerMixin, DeletionMixin):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = '/companies/brands'

    def post(self, request, pk):
        if 'confirm_delete' in self.request.POST:
            brand= Brand.objects.get(pk=pk)
            brand.delete()
        return super(BrandUpdateView, self).post(request, pk)
