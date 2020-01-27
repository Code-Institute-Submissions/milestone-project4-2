from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def all_jerseys(request):
    products = Product.objects.filter(category='jersey')
    return render(request, "products.html", {"products": products})

def all_shorts(request):
    products = Product.objects.filter(category='shorts')
    return render(request, "products.html", {"products": products})

def all_socks(request):
    products = Product.objects.filter(category='socks')
    return render(request, "products.html", {"products": products})

def all_base_layers(request):
    products = Product.objects.filter(category='base_layers')
    return render(request, "products.html", {"products": products})

def all_footballs(request):
    products = Product.objects.filter(category='football')
    return render(request, "products.html", {"products": products})

