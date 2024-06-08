from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer

from . import models


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token


class TelegramUserSerializer(ModelSerializer):
    class Meta:
        model = models.TelegramUser
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class UserOrderSerializer(ModelSerializer):
    class Meta:
        model = models.UserOrder
        fields = '__all__'
