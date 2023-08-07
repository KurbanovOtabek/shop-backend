from rest_framework import serializers
from .models import FavoriteItem, Product, CartItem, ProductColor, Order, Cart


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'author', 'name', 'price', 'image1', 'image2', 'image3', 'image4', 'image5', 'available', 'color', 'character',
                  'discount', 'slug', 'add_time', 'update_time']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'subtotal']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'name', 'phone_number', 'items', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cart = Cart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart


class OrderSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'