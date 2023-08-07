
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView

from .models import Product, FavoriteItem, CartItem, ProductColor, Order, Cart
from .serializers import ProductSerializer, CustomerSerializer, FavoriteItemSerializer, CartItemSerializer, \
    ColorSerializer, OrderSerializer, CartSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CustomerSerializer


class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class ColorViewSet(ListAPIView):
    queryset = ProductColor.objects.all()
    serializer_class = ColorSerializer


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CartRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'id'

