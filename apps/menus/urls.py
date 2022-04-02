from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView
from apps.menus.views import *
from apps.menus.views import ActiveMenuView, BrandMenuView, MenuDetailView


urlpatterns = [
    path('active/<brand_id>', ActiveMenuView.as_view()),
    path('m/<brand_id>', BrandMenuView.as_view(), name='brand-menus'),
    path('m/', BrandMenuView.as_view(), name='brand-menus'),
    path(
        'm/<brand_id>/detail/<menu_id>',
        MenuDetailView.as_view(),
        name='menu-detail'
    )
]
