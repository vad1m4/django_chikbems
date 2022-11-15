from django.urls import path
from .views import contacts, home, location, product_detail, products, template, shopping_cart
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home, name="home"),
    path("products/<int:pk>", product_detail, name="product_detail"),
    path("template/", template, name="template"),
    path("contacts/", contacts, name="contacts"),
    path("location/", location, name="location"),
    path("products/", products, name="products"),
    path("shopping_cart", shopping_cart, name="shopping_cart")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
