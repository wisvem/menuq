from apps.base.forms import RegisterForm
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(View):
    form_class = AuthenticationForm
    template = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        message = ''
        return render(
            request, self.template, {'form': form, 'message': message}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('/companies')
        message = 'Login Failed'
        return render(
            request,
            self.template,
            {'form': form, 'message': message}
        )

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/companies')
        return super().dispatch(*args, **kwargs)
