from apps.companies.models.company import Company
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from apps.companies.forms import CompanyForm

class CompanyView(ListView, LoginRequiredMixin, UpdateView):
    template_name = 'companies.html'
    model = Company
    form_class = CompanyForm
    success_url='/companies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companies = Company.objects.filter(created_by=self.request.user)
        context['companies'] = companies
        return context

    def get_object(self, queryset=None):
        try:
            return super(CompanyView, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CompanyView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CompanyView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CompanyView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
