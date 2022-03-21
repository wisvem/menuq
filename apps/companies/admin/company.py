from django.contrib import admin
from apps.companies.models.company import Company
from apps.companies.models.brand import Brand


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
