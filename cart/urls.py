from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_cart/<int:id>', views.add_cart, name='add_cart'),
    path("remove/<int:product_id>", views.remove, name="remove")
]
