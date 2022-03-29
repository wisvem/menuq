from ..models.brand import *
from django.contrib import admin
from apps.base.models.mixins import SaveAdminMixin


@admin.register(Company)
class CompanyAdmin(SaveAdminMixin):
    pass


@admin.register(Brand)
class BrandAdmin(SaveAdminMixin):
    pass
