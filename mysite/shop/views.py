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
    return render(request, "contacts.html",)

def location(request):
    return render(request, "location.html",)

def products(request):
    products = Product.objects.all()

    type_filter = request.GET.get("type","")
    type_var = ""
    if type_filter == "universal":
        type_var = "Universal"
        products = products.filter(type=type_var)
    elif type_filter == "outdoors":
        type_var = "Outdoors"
        products = products.filter(type=type_var)
    elif type_filter == "indoors":
        type_var = "Indoors"
        products = products.filter(type=type_var)

    has_nv_filter = request.GET.get("has_nightvision", "")
    nv_var = ""
    if has_nv_filter == 'true':
        nv_var = True
        products = products.filter(has_nightvision=nv_var)
    elif has_nv_filter == 'false':
        nv_var = False
        products = products.filter(has_nightvision=nv_var)

    sort_by = request.GET.get("sort", "new-to-old")
    if sort_by == "new-to-old":
        products = products.order_by("-id")
    elif sort_by == "old-to-new":
        products = products.order_by("id")
    elif sort_by == "high-to-low":
        products = products.order_by("-price")
    elif sort_by == "low-to-high":
        products = products.order_by("price")

    context = {
        "products": products, 
        "usd": usd,
        "nv_var": nv_var,
        "type_var": type_var,
    }
    return render(request, "products.html", context)