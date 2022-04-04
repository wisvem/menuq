from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView
from apps.menus.views import *
from apps.menus.views import (
    ActiveMenuView,
    BrandMenuView,
    MenuDetailView,

)


urlpatterns = [
    path(
        'active/<brand_id>',
        ActiveMenuView.as_view(),
        name='active-menu'
    ),
    path(
        'm/<brand_id>',
        BrandMenuView.as_view(),
        name='brand-menus'
    ),
    # this patern is activated whrn no bran_id is passed
    path(
        'm/',
        BrandMenuView.as_view(),
        name='brand-menus'
    ),
    path(
        'm/<brand_id>/detail/<menu_id>',
        MenuDetailView.as_view(),
        name='menu-detail'
    ),
    path(
        'menuedit/<brand_id>',
        MenuView.as_view(),
        name='menu-edit'
    )
]
