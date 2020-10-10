from django.shortcuts import render, redirect
from cart.models import Cart
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
 
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

# @login_required(login_url='/login/')
def add_cart(request, id):
    user = request.user
    product=Product.objects.get(id=id)
    if not Cart.objects.filter(user=user, product=product).exists():
        Cart.objects.create(user=user, product=product)
    return redirect("cart:cart")

def remove(request, product_id):
    user = request.user
    cart_item = Cart.objects.filter(user=user.id)
    if cart_item.filter(product_id=product_id):
        messages.success(request,'Item removed from cart successfully')
        cart_item.get(product_id=product_id).delete()
    else:
        messages.error(request,'Item is not in cart')
    return redirect("cart:cart")
