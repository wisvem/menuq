from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, FormView
from django.views.generic.detail import SingleObjectMixin

from apps.menus.form import MenuDetailFormset
from apps.menus.models import Menu


class MenuDetailEditView(FormView, SingleObjectMixin, LoginRequiredMixin):
    model = Menu
    template_name = 'menu_detail_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Menu.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Menu.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return MenuDetailFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse(
            "menu_detail", kwargs={
                "brand_id": self.object.brand_id,
                "menu_id": self.object.pk
            }
        )
    