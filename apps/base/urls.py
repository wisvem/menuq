from django.urls import path
from apps.base.views import Home, Login, Register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', Home.as_view()),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
