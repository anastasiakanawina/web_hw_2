from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_preview = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
