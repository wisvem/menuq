from django.urls import path
from apps.companies.views import *

urlpatterns = [
    path('', CompanyView.as_view(), name='companies'),
    path('brands/', BrandView.as_view(), name='brands')
]
