from django.shortcuts import render, get_list_or_404
from .models import Product
from django.views.generic import DetailView, ListView


class HomeView(ListView):
    template_name = 'main/home.html'
    model = Product
    paginate_by = 1


class ProductDetail(DetailView):
    template_name = "product/product-detail.html"
    model = Product


