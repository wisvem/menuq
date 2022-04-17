from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

from apps.base.models.mixins import OwnerMixin
from apps.companies.models import Brand
from apps.menus.form import CategoryFormSet


class CategoryUpdateView(OwnerMixin, FormView, SingleObjectMixin):
    model = Brand
    template_name = 'category_update.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Brand.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Brand.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return CategoryFormSet(
            **self.get_form_kwargs(),
            instance=self.object
        )

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'{self.object.name} categories has been updated'
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse(
            "category_update", kwargs={
                "pk": self.object.pk
            }
        )

