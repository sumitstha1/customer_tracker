from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_index, name='customer.index'),
    path('customers/create/', views.customer_create, name='customer.create'),
]
