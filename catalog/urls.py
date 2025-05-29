from django.urls import path

from catalog import views
from catalog.views import (
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    un_publish_product,
)

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", ProductCreateView.as_view(), name="create_product"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="edit_product"),
    path(
        "<int:pk>/delete/", ProductDeleteView.as_view(), name="product_confirm_delete"
    ),
    path(
        "un_publish_product/<int:product_id>/",
        un_publish_product,
        name="un_publish_product",
    ),
    path(
        "category/<int:category_id>/",
        views.CategoryListView.as_view(),
        name="category_list",
    ),
]
