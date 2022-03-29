from django.contrib import admin
from ..models.menu_detail import *
from apps.companies.models.brand import *
from apps.base.models.mixins import SaveAdminMixin


class InLineMenuDetail(admin.TabularInline):
    model = MenuDetail
    extra = 0
    readonly_fields = ['created_by', 'updated_by']


@admin.register(Menu)
class MenuAdmin(SaveAdminMixin):
    inlines = [
        InLineMenuDetail
    ]
    save_as = True
    list_select_related = True


@admin.register(Category)
class CategoryAdminView(SaveAdminMixin):
    list_select_related = True


@admin.register(Product)
class ProductAdminView(SaveAdminMixin):
    pass
