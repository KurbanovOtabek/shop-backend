from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

Author = get_user_model()


class ProductColor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Maxsulot rangi', blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name='Maxsulot nomi', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Maxsulot narxi')
    image1 = models.ImageField(upload_to="product/%Y-%M-%D/", null=True, blank=True, verbose_name="Product rasmi")
    image2 = models.ImageField(upload_to="product/%Y-%M-%D/", null=True, blank=True, verbose_name="Product rasmi")
    image3 = models.ImageField(upload_to="product/%Y-%M-%D/", null=True, blank=True, verbose_name="Product rasmi")
    image4 = models.ImageField(upload_to="product/%Y-%M-%D/", null=True, blank=True, verbose_name="Product rasmi")
    image5 = models.ImageField(upload_to="product/%Y-%M-%D/", null=True, blank=True, verbose_name="Product rasmi")
    available = models.BooleanField(default=True, verbose_name='Mahsulot mavjudligi')
    color = models.ManyToManyField(ProductColor, verbose_name='Maxsulot rangi', related_name='Rangi', blank=True)
    character = models.TextField(null=True, blank=True, verbose_name="Xarakteristika")
    discount = models.IntegerField(default=0, verbose_name='Skidka')
    slug = models.SlugField(max_length=50, unique=True)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulot'

    def __str__(self):
        return self.name


class FavoriteItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Cart(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def subtotal(self):
        return self.product.price * self.quantity


# class CartItem(models.Model):
#     customer = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.product.name} ({self.quantity})"
#
#     def save(self, *args, **kwargs):
#         self.price = self.product.price * self.quantity
#         super().save(*args, **kwargs)


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(CartItem)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'
