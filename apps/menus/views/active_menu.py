from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View
from apps.menus.models.menu import *


class ActiveMenuView(ListView):
    template_name = 'active_menu.html'
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.get_queryset()
        return context

    def get_queryset(self):
        self.brand = Brand.objects.get(pk=self.kwargs['brand_id'])
        return Menu.objects.filter(is_active=True, brand=self.brand).first()