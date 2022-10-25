from django.db import models



class Product(models.Model):
    types = [("Outdoors", "Outdoors"), ("Indoors", "Indoors"), ("Universal", "Universal")]
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=255, choices=types)
    has_nightvision = models.BooleanField(default=False)
    pictures = models.ImageField(upload_to="cameras")
    usd = 37

    def __str__(self):
        return self.title
