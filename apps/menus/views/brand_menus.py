from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View
from apps.menus.models.menu import *
from django.http import Http404
from django.shortcuts import get_object_or_404

class BrandMenusView(ListView):
    template_name = 'brand_menus.html'
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = self.get_queryset()
        return context

    def get_queryset(self):
        #self.brand = Brand.objects.get(pk=self.kwargs['brand_id'])
        self.brand = get_object_or_404(Brand, pk=self.kwargs['brand_id'])
        self.user = self.request.user
        if self.user.id is not self.brand.created_by.id:
            raise Http404()
        return Menu.objects.filter(brand=self.brand, created_by=self.user)
