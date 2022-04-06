from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView

from apps.menus.models.menu_detail import *


class MenuDetailView(ListView, LoginRequiredMixin):
    template_name = 'menu_detail.html'
    model = MenuDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.get_queryset()
        return context

    def get_queryset(self):
        self.menu = Menu.objects.get(pk=self.kwargs['menu_id'])
        self.user = self.request.user
        if self.user.id is not self.menu.created_by.id:
            raise Http404()
        return self.menu
