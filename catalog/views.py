from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView, CreateView

from .forms import ProductForm
from .models import Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('catalog:product_list')

    def create_product(request):
        if request.POST == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('catalog:product_list')
        else:
            form = ProductForm()
        return render(request, 'catalog/create_product.html', {'form': form})

    def product_confirm_delete(self):
        Product.objects.filter(id=self).delete()



class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
