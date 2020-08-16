from django.shortcuts import render, redirect
from .models import Cart
from django.http import HttpResponse
from products.models import Product

 
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user.id).order_by('-updated')
    total, discount, mrp = 0,0,0
    for i in cart_items:
        mrp += i.product.mrp
        total += i.product.deal_price
        discount += (i.product.mrp - i.product.deal_price)
    context={
        'cart_items':cart_items,
        'mrp':mrp,
        'total':total,
        'discount':discount
        }
    return render(request, 'cart/cart.html', context)

def add_cart(request, id):
    user = request.user
    product=Product.objects.get(id=id)
    if not Cart.objects.filter(user=user, product=product).exists():
        Cart.objects.create(user=user, product=product)
    return redirect("cart:cart")

def remove(request, product_id):
    user = request.user
    cart_item = Cart.objects.filter(user=user.id)
    cart_item.get(product_id=product_id).delete()
    return redirect("cart:cart")
