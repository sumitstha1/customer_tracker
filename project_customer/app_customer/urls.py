from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_index, name='customer.index'),
    path('customers/create/', views.customer_create, name='customer.create'),
    path('customers/update/', views.customer_update, name='customer.update'),
    path('customers/edit/<int:id>/', views.customer_edit, name='customer.edit'),
]
