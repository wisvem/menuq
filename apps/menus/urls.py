from django.urls import path
from apps.menus.views import (
    MenuActiveView,
    MenuListView,
    MenuDetailView,
    MenuDetailEditView
)


urlpatterns = [
    path(
        'active/<brand_id>/',
        MenuActiveView.as_view(),
        name='active_menu'
    ),
    path(
        'm/<brand_id>/',
        MenuListView.as_view(),
        name='list_menus'
    ),
    # this pattern is activated when no bran_id is passed
    path(
        'm/',
        MenuListView.as_view(),
        name='list_menus'
    ),
    path(
        'm/<brand_id>/detail/<menu_id>/',
        MenuDetailView.as_view(),
        name='menu_detail'
    ),
    path(
        'm/<pk>/edit/',
        MenuDetailEditView.as_view(),
        name='menu_edit'
    )
]
