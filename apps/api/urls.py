"""API URLS"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views.category import CategoryViewSet
from apps.api.views.product_price import ProductPriceViewSet
from apps.api.views.price_list import PriceListViewSet
from apps.api.views.product import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'prices', ProductPriceViewSet)
router.register(r'pricelists', PriceListViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
