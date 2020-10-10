from django.shortcuts import render, redirect
from .models import *
from cart.models import Cart
import math
from django.template.defaulttags import register
from django.contrib.auth.models import User



def index(request):
    banners = Banner.objects.all().order_by("-created_at").first()
    laptops = Product.objects.filter(category_id=2)
    return render(request, "index.html", context={'banners':banners, 'laptops':laptops})

def laptops(request):
    products = Product.objects.filter(category_id=2)
    context = {'products':products,
                }
    return render(request, "products/categories.html", context)

def mobiles(request):
    products = Product.objects.filter(category_id=1)
    context = {'products':products}
    return render(request, "products/categories.html", context)

def sensors(request):
    products = Product.objects.filter(category_id=3)
    context = {'products':products}
    return render(request, "products/categories.html", context)

def electronic_components(request):
    products = Product.objects.filter(category_id=4)
    context = {'products':products}
    return render(request, "products/categories.html", context)

def rating(request, id):
    rating = id
    context = {'rating':rating}
    print(rating)
    return reverse("laptops", context)

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    rating = list(range(product.rating))
    user = request.user
    cart = []
    if user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        for i in cart_items:
            cart.append(i.product.id)
    rating_un = list(range(5-len(rating)))
    save = ((product.mrp-product.deal_price)/product.mrp)*100
    context = {
        'product':product,
        'rating': rating,
        'rating_un': rating_un,
        'cart':cart,
        'save': save
    }
    return render(request, "products/product_descr.html", context)