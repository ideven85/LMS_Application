
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)


class Photo(models.Model):
    product = models.ForeignKey(Product, related_name="photos",
                                on_delete=models.CASCADE)
    image = models.ImageField(blank=True)