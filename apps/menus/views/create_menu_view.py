from apps.menus.models.menu_detail import *
from django.views.generic import CreateView
from apps.menus.form import *


class CreateMenuView(CreateView):
    form_class = CreateMenuForm
    template_name = "menu_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreateMenuView, self).get_context_data(**kwargs)
        context ['menu_detail_formset'] = MenuDetailInlineFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get(form_class)
        menu_detail_formset = MenuDetailInlineFormset(self.request.POST)
        if form.is_valis() and menu_detail_formset.is_valid():
            return self.form_valid(form, menu_detail_formset)
        else:
            return self.form_invalid(form, menu_detail_formset)
    
    def form_valid(self, form, menu_detail_formset):
        self.object = form.save(commit=False)
        self.object.save()
        # saving menu detial Instances
        menu_detail = menu_detail_formset.save(commit=False)
        for item in menu_detail:
            item.menu = self.object
            item.save()
        return redirect(reverse(''))

    def form_invalid(self, form, menu_detail_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                menu_detail_formset=menu_detail_formset
            )
        )
