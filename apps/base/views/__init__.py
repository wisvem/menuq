from apps.base.forms import RegisterForm
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render


class Register(View):
    form_class = RegisterForm
    template_name = 'register.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valis():
            return HttpResponseRedirect('/index/')
        return render(request, self.template_name, {'form': form})
