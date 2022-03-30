from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView
from apps.menus.views import *

urlpatterns = [
    path('<int:brand_id>/', create, name='menu'),
]
