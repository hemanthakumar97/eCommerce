from django.shortcuts import render,redirect
from .models import *
import math


def index(request):
    return render(request, "index.html")

def laptops(request):
    laptops = Product.objects.filter(category_id=2)
    context = {'laptops':laptops}
    return render(request, "products/categories.html", context)

def mobiles(request):
    mobiles = Product.objects.filter(category_id=1)
    context = {'mobiles':mobiles}
    return render(request, "products/categories.html", context)

def sensors(request):
    sensors = Product.objects.filter(category_id=3)
    context = {'sensors':sensors}
    return render(request, "products/categories.html", context)

def electronic_components(request):
    electronic_components = Product.objects.filter(category_id=4)
    context = {'electronic_components':laptops}
    return render(request, "products/categories.html", context)

def product(request):
    product = Product.objects.get(id=10)
    rating = list(range(product.rating))
    rating_un = list(range(5-len(rating)))
    save = ((product.mrp-product.deal_price)/product.mrp)*100
    context = {
        'product':product,
        'rating': rating,
        'rating_un': rating_un,
        'save': save
    }
    return render(request, "products/product_descr.html", context)