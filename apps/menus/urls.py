from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView
from apps.menus.views import *
from apps.menus.views import ActiveMenuView


urlpatterns = [
    path('active/<brand_id>', ActiveMenuView.as_view()),
]
