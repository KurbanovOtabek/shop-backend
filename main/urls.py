from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CustomerViewSet, FavoriteItemViewSet, CartItemViewSet, ColorViewSet, OrderView, \
    CartRetrieveUpdateView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'favorites', FavoriteItemViewSet)
router.register(r'cart', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('color', ColorViewSet.as_view()),
    path('orders/', OrderView.as_view()),
    path('carts/<int:id>/', CartRetrieveUpdateView.as_view()),
]
