from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    types = [("Outdoors", "Outdoors"), ("Indoors", "Indoors"), ("Universal", "Universal")]
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=255, choices=types)
    has_nightvision = models.BooleanField(default=False)
    pictures = models.ImageField(upload_to="cameras")

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)