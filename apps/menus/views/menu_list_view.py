from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import resolve
from django.views.generic import ListView, UpdateView

from apps.menus.form import MenuCreateForm
from apps.menus.models.menu import *


class MenuListView(ListView, LoginRequiredMixin, UpdateView):
    template_name = 'menu_list.html'
    model = Menu
    form_class = MenuCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = self.get_queryset()
        if hasattr(self, 'brand'):
            context['brand'] = self.brand
        return context

    def get_queryset(self):
        self.user = self.request.user
        if self.kwargs.get('brand_id', None) is None:
            return Menu.objects.filter(created_by=self.user)
        self.brand = get_object_or_404(Brand, pk=self.kwargs['brand_id'])
        if self.user.id is not self.brand.created_by.id:
            raise Http404()
        return Menu.objects.filter(
            brand=self.brand,
            created_by=self.user
        ).order_by('-is_active', 'name')


    def get_object(self, queryset=None):
        try:
            return super(MenuListView, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(MenuListView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'activate' in request.POST:
            menu = Menu.objects.get(pk=request.POST.get('menu_id'))
            menu.is_active = True
            menu.save()
            messages.add_message(
                self.request, 
                messages.SUCCESS,
                f'{menu.name} has been activated'
            )
            return HttpResponseRedirect(request.build_absolute_uri())
        else:
            self.object = self.get_object()
            return super(MenuListView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(MenuListView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        kwargs.update({'brand': self.kwargs.get('brand_id')})
        return kwargs

    def form_valid(self, form):

        messages.add_message(
            self.request, 
            messages.SUCCESS,
            'The menu has been created correctly'
        )

        return super().form_valid(form)
