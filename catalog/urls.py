from django.urls import path

from catalog import views
from .views import product_list, product_detail

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_list/', product_list, name='product_list'),
    path("product_detail/<int:product_id>", product_detail, name="product_detail"),
]
