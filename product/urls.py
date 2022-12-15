from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product_detail')
]