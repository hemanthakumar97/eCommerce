from django.contrib import admin
from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('laptops/', views.laptops, name='laptops'),
    path('mobiles/', views.mobiles, name='mobiles'),
    path('sensors/', views.sensors, name='sensors'),
    path('electronic_components/', views.electronic_components, name='electronic_components'),
]