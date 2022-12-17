from django.db import models


CATEGORY_CHOICES = (
    ('M', "Erkaklar"),
    ('W', "Atollar"),
    ('Ch', "Bolalar")
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

"""Maxsulotlar uchun model"""
class Product(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
