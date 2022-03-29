from django.urls import path
from apps.companies.views import *

urlpatterns = [
    path('', CompanyView.as_view()),
    path('brands/', BrandView.as_view(success_url='/companies/brands'))
]
