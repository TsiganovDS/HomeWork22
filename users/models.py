from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        validators=[RegexValidator(r"^\+?\d{9,15}$", message="Пример: '+79999999999'")],
    )
    country = CountryField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
