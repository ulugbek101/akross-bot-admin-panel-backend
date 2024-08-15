from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        statuses = {
            'bronze': '🥉 Bronze',
            'silver': '🥈 Silver',
            'gold': '🥇 Gold',
            'platinum': '🌟 Platinum',
        }
        representation['status'] = statuses[instance.status]
        return representation


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
    product = ProductSerializer(read_only=True)
    product_id = PrimaryKeyRelatedField(queryset=models.Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = models.Order
        fields = '__all__'


class UserOrderSerializer(ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    user = TelegramUserSerializer(read_only=True)
    user_id = PrimaryKeyRelatedField(queryset=models.TelegramUser.objects.all(), source='user', write_only=True)

    class Meta:
        model = models.UserOrder
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Fetch related orders for the specific instance
        orders = models.Order.objects.filter(order_id=instance.id)
        orders = OrderSerializer(orders, many=True).data

        representation['orders'] = orders
        return representation
