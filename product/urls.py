from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', home, name='home'),

    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product_detail')
]