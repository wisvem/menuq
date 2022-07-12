from django.core.serializers import serialize
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from apps.companies.models import Brand
from apps.menus.models import Menu


class MenuActiveView(ListView):
    template_name = 'active_menu.html'
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand'] = self.brand
        context['menu'] = self.get_queryset()
        items = [
            {
                'product': x.product,
                'price': x.price,
                'category': x.category
            } for x in context['menu'].menu_details.all()
        ]
        context['items'] = items


        return context

    def get_queryset(self):
        #self.brand = Brand.objects.get(pk=self.kwargs['brand_id'])
        self.brand = get_object_or_404(Brand, pk=self.kwargs['brand_id'])
        return Menu.objects.filter(is_active=True, brand=self.brand).first()
