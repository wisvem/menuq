from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView
from apps.products.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:menu_id>/', detail, name='detail'),
    path('<int:menu_id>/results/', results, name='results'),
    path('<int:menu_id>/vote/', create, name='create'),
]
