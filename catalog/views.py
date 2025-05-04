from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})


