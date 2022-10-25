from django.urls import path
from .views import home, product_detail, template
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home, name="home"),
    path("products/<int:pk>", product_detail, name="product_detail"),
    path("template/", template, name="template"),
    path("contacts/", template, name="comtact-info"),
    path("location/", template, name="location"),
    path("products/", template, name="products"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)