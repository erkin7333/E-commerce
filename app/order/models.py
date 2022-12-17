from django.db import models
from django.conf import settings
from product.models import Product



"""Buyurtma elementlari uchun model"""
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



"""Buyurtmalar uchun model"""
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
