from django.contrib import admin
from django.urls import path
from .views import *
app_name= 'buy'

urlpatterns = [
    path("payment/<int:id>/", payment, name='payment'),
    path("address/", address, name='address'),
]