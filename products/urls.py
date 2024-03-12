from django.contrib import admin
from django.urls import path
from .views import products, basket_add

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
]
