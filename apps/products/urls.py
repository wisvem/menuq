from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', HttpResponse("Index page of menuq"))
]
