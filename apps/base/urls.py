from django.urls import path
from apps.base.views import Home, Login, Register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', Home.as_view()),
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', LogoutView.as_view())
]
