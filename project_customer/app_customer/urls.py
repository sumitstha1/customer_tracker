from django.urls import path
from . import views

urlpatterns = [

    # users urls
    path('users/register/', views.user_register, name='user.register'),

    # customers urls
    path('customers/', views.customer_index, name='customer.index'),
    path('customers/show/<int:id>/', views.customer_show, name='customer.show'),
    path('customers/create/', views.customer_create, name='customer.create'),
    path('customers/update/', views.customer_update, name='customer.update'),
    path('customers/edit/<int:id>/', views.customer_edit, name='customer.edit'),
    path('customers/delete/<int:id>/', views.customer_delete, name='customer.delete'),
]
