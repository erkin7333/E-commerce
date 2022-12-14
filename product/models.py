from django.db import models


"""Maxsulotlar uchun model"""
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
