from django.contrib.auth import get_user_model

User = get_user_model()
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name", "description"]

    def __str__(self):
        return f"{self.name} {self.description}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=False)

    class Meta:
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "category", "price"]

    def __str__(self):
        return f"{self.name} {self.description}"
