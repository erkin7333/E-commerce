from django.shortcuts import render, get_list_or_404
from .models import Product
from django.views.generic import DetailView

def home(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'main/home.html', context=context)


class ProductDetail(DetailView):
    template_name = "product/product-detail.html"
    model = Product


