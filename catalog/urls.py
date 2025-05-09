from django.urls import path

from blog.views import BlogListView
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('', BlogListView.as_view(), name='blog_list'),
]
