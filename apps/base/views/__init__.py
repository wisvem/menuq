from apps.base.forms import RegisterForm
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


class Register(View):
    form_class = RegisterForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='clients')
            user.groups.add(group)
            return redirect('/login')
        return render(request, self.template_name, {'form': form})


class Login(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        message = ''
        return render(
            request, self.template_name, {'form': form, 'message': message}
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
                return redirect('/admin')
        message = 'Login Failed'
        return render(
            request,
            self.template_name,
            {'form': form, 'message': message}
        )
