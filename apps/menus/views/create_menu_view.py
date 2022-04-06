from apps.menus.models.menu_detail import *
from django.views.generic import CreateView
from apps.menus.form import *
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateMenuView(CreateView, LoginRequiredMixin):
    form_class = CreateMenuForm
    template_name = "menu_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreateMenuView, self).get_context_data(**kwargs)
        context ['menu_detail_form'] = MenuDetailFormset()
        brand = Brand.objects.get(pk=self.kwargs.get('brand_id'))
        for form in context['menu_detail_form']:
            form.fields['category'].queryset = Category.objects.filter(brand=brand)
            form.fields['product'].queryset = Product.objects.filter(brand=brand)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        menu_detail_form = MenuDetailFormset(self.request.POST)
        if form.is_valid() and menu_detail_form.is_valid():
            return self.form_valid(form, menu_detail_form)
        else:
            return self.form_invalid(form, menu_detail_form)
    
    def form_valid(self, form, menu_detail_form):
        self.object = form.save(commit=False)
        self.object.save()
        # saving menu detial Instances
        menu_detail = menu_detail_form.save(commit=False)
        for item in menu_detail:
            item.menu = self.object
            item.save()
        return redirect(reverse(''))

    def form_invalid(self, form, menu_detail_form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                menu_detail_form=menu_detail_form
            )
        )

    def get_form_kwargs(self):
        kwargs = super(CreateMenuView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        kwargs.update({'brand': self.kwargs.get('brand_id')})
        return kwargs
