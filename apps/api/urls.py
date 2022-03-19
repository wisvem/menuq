"""API URLS"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.api.views.product import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'prices', ProductViewSet)
router.register(r'pricelists', ProductViewSet)
router.register(r'categories', ProductViewSet)
urlpatterns = [
    path('products/', include(router.urls))
]
