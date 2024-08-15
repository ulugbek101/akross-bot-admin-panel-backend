from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from . import views

router = DefaultRouter()

router.register(basename='telegram-users', viewset=views.TelegramUserViewSet, prefix='telegram-users')
router.register(basename='categories', viewset=views.CategoryViewSet, prefix='categories')
router.register(basename='products', viewset=views.ProductViewSet, prefix='products')
router.register(basename='locations', viewset=views.LocationViewSet, prefix='locations')
router.register(basename='carts', viewset=views.CartViewSet, prefix='carts')
router.register(basename='orders', viewset=views.OrderViewSet, prefix='orders')
router.register(basename='user-orders', viewset=views.UserOrderViewSet, prefix='user-orders')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
