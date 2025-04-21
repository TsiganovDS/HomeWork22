from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
]






