from django.contrib import admin
from ..models.menu_detail import *
from apps.companies.models.brand import *


class InLineMenuDetail(admin.TabularInline):
    model = MenuDetail
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [
        InLineMenuDetail
    ]
    save_as = True
    list_select_related = True


@admin.register(Category)
class CategoryAdminView(admin.ModelAdmin):
    list_select_related = True


@admin.register(Product)
class ProductAdminView(admin.ModelAdmin):
    pass
