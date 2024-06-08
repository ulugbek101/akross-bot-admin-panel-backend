from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class TelegramUserViewSet(ModelViewSet):
    queryset = models.TelegramUser.objects.all()
    serializer_class = serializers.TelegramUserSerializer


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class LocationViewSet(ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer


class CartViewSet(ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer


class OrderViewSet(ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class UserOrderViewSet(ModelViewSet):
    queryset = models.UserOrder.objects.all()
    serializer_class = serializers.UserOrderSerializer
