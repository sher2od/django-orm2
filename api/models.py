from django.db import models

# Create your models here

class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    price  = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    rating = models.DecimalField(max_digits=3,decimal_places=1)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product(id={self.id}, name="{self.name}")'

