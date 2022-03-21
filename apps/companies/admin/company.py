from ..models.company import Company
from django.contrib import admin

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
