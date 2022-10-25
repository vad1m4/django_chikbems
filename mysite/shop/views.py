from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all().order_by("-id")
    return render(request, "home.html", {"products": products, "usd": usd})

usd = 37

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product.html", {"product": product, "usd": usd})

def template(request):
    return render(request, "template.html",)

def contacts(request):
    return render(request, "contact-info.html",)

def location(request):
    return render(request, "location.html",)

def products(request):
    return render(request, "products.html",)