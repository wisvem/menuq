from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView

from apps.companies.forms import BrandForm
from apps.companies.models.brand import Brand


class BrandView(ListView, LoginRequiredMixin, UpdateView):
    template_name = 'brands.html'
    model = Brand
    form_class = BrandForm
    success_url = '/companies/brands'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.filter(
            created_by=self.request.user
            ).order_by('name')
        context['brands'] = brands
        return context

    def get_object(self, queryset=None):
        try:
            return super(BrandView, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(BrandView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(BrandView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(BrandView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
