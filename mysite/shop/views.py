from django.shortcuts import render
from .models import Product
from .filters import ProductFilter

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
    if type_filter == "universal":
        products = products.filter(type="Universal")
        print("UNIVERSAL")
    elif type_filter == "outdoors":
        products = products.filter(type="Outdoors")
    elif type_filter == "indoors":
        products = products.filter(type="Indoors")
    # types = request.GET.getlist('type')
    # for type in types:
    #     products = products.filter(type=type)

    has_nv_filter = request.GET.get("has_nv", "")
    if has_nv_filter == 'yes':
        products = products.filter(has_nightvision=True)
    elif has_nv_filter == 'no':
        products = products.filter(has_nightvision=False)

    sort_by = request.GET.get("sort", "new-to-old")
    if sort_by == "new-to-old":
        products = products.order_by("-id")
    elif sort_by == "old-to-new":
        products = products.order_by("id")
    elif sort_by == "high-to-low":
        products = products.order_by("-price")
    elif sort_by == "low-to-high":
        products = products.order_by("price")

    products_filter = ProductFilter(request.GET, queryset=products)
    context = {
        "products": products, 
        "usd": usd,
        "products_filter": products_filter,
    }
    return render(request, "products.html", context)