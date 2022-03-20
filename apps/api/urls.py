"""API URLS"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views.category import CategoryViewSet
from apps.api.views.menu import MenuViewSet
from apps.api.views.product import ProductViewSet
#from apps.api.views.product_category import ProductCategoryViewSet
from apps.api.views.menu_detail import MenuDetailViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'prices', MenuDetailViewSet)
router.register(r'pricelists', MenuViewSet)
router.register(r'categories', CategoryViewSet)
#router.register(r'productcategory', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
