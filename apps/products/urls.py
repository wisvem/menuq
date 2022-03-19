from django.urls import path
from django.views.generic import TemplateView
from django.http import HttpResponse

urlpatterns = [
    path('index/', HttpResponse("Index page of menuq"))
]
