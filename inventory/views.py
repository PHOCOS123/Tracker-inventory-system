from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request,"inventory/categories.html")


def dashboard(request):
    return render(request,"inventory/dashboard.html")


def products(request):
    return render(request,"inventory/products.html")

def sales(request):
    return render(request,"inventory/sales.html")


def stock(request):
    return render(request,"inventory/stock.html")

def suppliers(request):
    return render(request,"inventory/supplier.html")

def users(request):
    return render(request,"inventory/users.html")