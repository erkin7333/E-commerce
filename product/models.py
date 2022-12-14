from django.db import models


"""Maxsulotlar uchun model"""
class Product(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product')
    price = models.FloatField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
