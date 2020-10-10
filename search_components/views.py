from django.shortcuts import render, redirect
from products.models import Product, Category

def search(request):
    search_input = request.POST["inp"]
    products = Product.objects.filter(title__icontains=search_input, is_published=True).order_by("-updated_at")
    
    if len(products)==0 and search_input=="mobiles" or search_input=="mobile":
        products = Product.objects.filter(category=1).order_by("-updated_at")

    if len(products)==0 and search_input=="laptops" or search_input=="laptop":
        products = Product.objects.filter(category=2).order_by("-updated_at")

    if len(products)==0 and search_input=="sensors" or search_input=="sensor":
        products = Product.objects.filter(category=3).order_by("-updated_at")

    if len(products)==0 and search_input=="electronic components" or search_input=="electronic component":
        products = Product.objects.filter(category=4).order_by(-id).order_by("-updated_at")
    return render(request, "products/categories.html", context={"products":products, "search_input":search_input})
    


