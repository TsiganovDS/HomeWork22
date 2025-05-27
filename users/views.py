from urllib import request

from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from catalog.models import Product
from users.forms import CustomUserCreationForm


class HomeView(CreateView):
    template_name = "users/login.html"


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = "dm.tsiganov@gmail.com"
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class LoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("catalog:home")


class LogoutView(LogoutView):
    next_page = reverse_lazy("catalog:home")
