from django.contrib import admin
from django.urls import path
from .views import *
app_name= 'buy'

urlpatterns = [
    path("payment/<int:id>/", payment, name='payment'),
    path("address/", address, name='address'),
    path("place_order/", place_order, name='place_order'),
    path("confirm_page/", confirm_page, name='confirm_page'),
    path("my_orders/", my_orders, name='my_orders'),
    # path("email/", email, name='email'),
]