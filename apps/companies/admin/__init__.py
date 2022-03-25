from ..models.brand import *
from django.contrib import admin

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
