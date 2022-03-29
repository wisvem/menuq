from apps.companies.models.company import Company
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

class CompanyView(ListView, LoginRequiredMixin):
    template_name = 'companies.html'
    model = Company
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        companies = Company.objects.filter(created_by=self.request.user)
        context['companies'] = companies
        return context

