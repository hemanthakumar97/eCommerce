from django.shortcuts import render,redirect
from .models import *
import math


def index(request):
    return render(request, "index.html")

def product(request):
    product = Product.objects.get(id=5)
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