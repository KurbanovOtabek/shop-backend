from django.contrib import admin

from main.models import FavoriteItem, Product, CartItem, ProductColor, Order, Cart

admin.site.register(FavoriteItem)
admin.site.register(ProductColor)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display_links = ("author",)
    list_filter = ("author", "add_time", "update_time")
    filter_horizontal = ["color"]
    list_display = (
        "id", "author", "name", "price", "available",
        "discount", "add_time", "update_time")


"сделай мне логику покупки товара с ценой оформлением заказа по имени и номера в корзине на django rest framework"