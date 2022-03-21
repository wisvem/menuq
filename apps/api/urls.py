"""API URLS"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views.category import CategoryViewSet
from apps.api.views.menu import MenuViewSet
from apps.api.views.menu_detail import MenuDetailViewSet
from apps.api.views.product import ProductViewSet
from apps.api.views.company import CompanyViewSet
from apps.api.views.brand import BrandViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'menudetail', MenuDetailViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'companies', CategoryViewSet)
router.register(r'brands', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls))
]
