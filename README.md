# Inventory Tracker
#For an inventory tracker, you’ll probably create:

Products
Categories
Suppliers
Stock movement
Sales
Users
Dashboard

Example of how to connect your HTML
in index.html
#{% load static %}

#<!-- <!DOCTYPE html>
#<html>
<head>
    <title>Inventory Tracker</title>

    <link rel="stylesheet" href="{% static 'inventory/css/style.css' %}">
</head>
<body>

    <h1>Tracker Inventory System</h1>

    <script src="{% static 'inventory/js/script.js' %}"></script>
</body>
</html> -->


How Django show pages
in viewa.py
<!-- 
from django.shortcuts import render

def home(request):
    return render(request, 'inventory/index.html')
 -->

Create URLs
inside inventory/urls.py
<!-- 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
] -->


How to connect app URLs to main Project
Inside config/urls.py
<!--
 from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
] 
-->