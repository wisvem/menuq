from apps.companies.models.brand import Brand
from apps.companies.models.company import Company
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from apps.companies.forms import BrandForm
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.views.generic import UpdateView
from django.urls import reverse


class BrandView(ListView, LoginRequiredMixin, UpdateView):
    template_name = 'brands.html'
    model = Brand
    #fields = ['name', 'description', 'company']
    form_class = BrandForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brands = Brand.objects.filter(created_by=self.request.user)
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
