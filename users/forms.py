from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data["email"]
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Пользователь с такой электронной почтой уже зарегистрирован."
            )

        return email
