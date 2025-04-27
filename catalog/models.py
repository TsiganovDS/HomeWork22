from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField()
    purchase_price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

def __str__(self):
    return f'{self.name} {self.description}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()