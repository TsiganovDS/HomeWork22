from urllib import request

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProductForm, ProductModeratorForm
from .models import Product


def user_can_unpublish(user):
    return user.has_perm("catalog.can_unpublish_product")


@user_passes_test(user_can_unpublish)
def un_publish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.is_published = False
    product.save()
    return redirect("catalog:product_list")


@login_required
def can_delete_any_product(product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.has_perm("catalog.can_delete_product"):
        product.delete()
        return redirect("product_list")
    else:
        return redirect("catalog:home")


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/create_product.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    @login_required
    def create_product(request):
        if request.method == "POST":
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.owner = request.user
                product.save()
                return redirect("product_list")
        else:
            form = ProductForm()
        return render(request, "create_product.html", {"form": form})

    def product_confirm_delete(self):
        Product.objects.filter(id=self).delete()

    def get_form_class(self):
        user = self.request.user
        if user.is_authenticated:
            if self.object and user == self.object.owner:
                return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm(
            "catalog.can_delete_product"
        ):
            return ProductModeratorForm
        raise PermissionDenied

    def get_object(self, queryset=None):
        self.user = super().get_object()
        if self.request.user == self.object.owner:
            return ProductForm


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/edit_product.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    @login_required
    def delete_product(request, product_id):
        product = Product.objects.get(id=product_id)
        if product.owner != request.user and not request.user.is_staff:
            return HttpResponseForbidden()

        product.delete()
        return redirect("product_list")


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.owner != request.user and not request.user.is_staff:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("catalog:product_detail.html", product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, "catalog:edit_product.html", {"form": form})
