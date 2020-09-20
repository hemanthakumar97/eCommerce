from django.shortcuts import render, redirect
from products.models import Product
from user_profile.models import *
from .models import *


def payment(request,id):
    user = request.user
    if request.method=="POST":
        inp = request.POST['payment_mode']
        product = Product.objects.get(id=id)
        Order.objects.create(user=user, product=product, payment_method=inp)
        return redirect("buy:address")
    return render(request, "buy/payment.html")

def address(request):
    user = request.user
    if request.method=="POST":
        id = request.POST['address']
        obj = Address.objects.get(id=id)
        Order.objects.update(user=user, address=obj)
        return redirect("buy:place_order")
    addresses = Address.objects.filter(user=user)
    return render(request, "buy/address.html",{"addresses":addresses})

def place_order(request):
    if request.method=="POST":
        return redirect("buy:confirm_page")
    address = Order.objects.get(id=5).address
    return render(request, "buy/place_order.html",{"address":address})

def confirm_page(request):
    address = Order.objects.get(id=5).address
    return render(request,"buy/confirm_page.html",{"address":address})