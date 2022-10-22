from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all().order_by("-id")
    return render(request, "home.html", {"products": products})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product.html", {"product": product})
