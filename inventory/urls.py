from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('',views.categories,name='categories'),
    path('',views.products,name='product'),
    path('',views.sales,name='sales'),
    path('',views.stock,name='stocks'),
    path('',views.suppliers,name='suppliers'),
    path('',views.users,name='users')
]