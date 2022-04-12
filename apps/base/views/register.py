from apps.base.forms import RegisterForm
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.urls import reverse


class Register(View):
    form_class = RegisterForm
    template = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='clients')
            user.groups.add(group)
            return redirect(reverse('login'))
        return render(request, self.template, {'form': form})
