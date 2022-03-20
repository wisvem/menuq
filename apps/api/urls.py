"""API URLS"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views.category import CategoryViewSet
from apps.api.views.price_list import PriceListViewSet
from apps.api.views.product import ProductViewSet
#from apps.api.views.product_category import ProductCategoryViewSet
from apps.api.views.product_price import ProductPriceViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'prices', ProductPriceViewSet)
router.register(r'pricelists', PriceListViewSet)
router.register(r'categories', CategoryViewSet)
#router.register(r'productcategory', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
