from django.shortcuts import render
from .models import Product


def product_list(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'product/product-list.html', context=context)