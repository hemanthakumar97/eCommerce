from django.shortcuts import render, redirect
from products.models import Product
from user_profile.models import *
from django.core.mail import EmailMessage, EmailMultiAlternatives
from .models import *
from django.template.loader import render_to_string, get_template
from django.contrib.auth.models import User


def payment(request,id):
    user = request.user
    if request.method=="POST":
        inp = request.POST['payment_mode']
        product = Product.objects.get(id=id)
        order = Order.objects.create(user=user, product=product, payment_method=inp)
        request.session["order_id"] = order.id
        return redirect("buy:address")
    return render(request, "buy/payment.html")

def address(request):
    user = request.user
    if request.method=="POST":
        id = request.POST['address']
        obj = Address.objects.get(id=id)
        order_id = request.session["order_id"]
        address = Order.objects.get(id=order_id)
        address.address=obj
        address.save()
        return redirect("buy:place_order")
    addresses = Address.objects.filter(user=user)
    return render(request, "buy/address.html",{"addresses":addresses})

def place_order(request):
    order_id = request.session["order_id"]
    buy = Order.objects.get(id=order_id)
    product = buy.product
    address = buy.address
    if request.method=="POST":
        order_id = request.session["order_id"]
        order = Order.objects.get(id=order_id)
        order.confirm=True
        order.save()
        mail_subject = 'Order Placed'
        message = render_to_string('email_confirm.html', {
                    'product': product,
                    'address': address,
                })
        to_email = User.objects.get(id=request.user.id).email
        email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
        email.attach_alternative(message, "text/html")
        email.send()
        return redirect("buy:confirm_page")
    return render(request, "buy/place_order.html",{"product":product ,"address":address})

def confirm_page(request):
    order_id = request.session["order_id"]
    address = Order.objects.get(id=order_id).address
    return render(request,"buy/confirm_page.html",{"address":address})

def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,"buy/my_orders.html",context={"orders":orders})