from django.urls import path, include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('products/', include(router.urls)),
    path('products/<int:pk>', include(router.urls))
    ]


