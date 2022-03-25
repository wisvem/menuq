from django.urls import path
from apps.base.views import Register


urlpatterns = [
    path('register/', Register.as_view()),
]
