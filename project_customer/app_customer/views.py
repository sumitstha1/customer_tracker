from venv import create
from django.shortcuts import render

from app_customer.forms import CustomerCreateForm

# Create your views here.
def customer_index(request):
    template = 'customers/index.html'
    contex = {
        "data": {
            "first_name": "Maila",
            "last_name": "Byakul",
            "email": "byakul@gmail.com"
        }
    }
    return render(request, template, contex)

def customer_create(request):
    create_form = CustomerCreateForm()
    context = {"form": create_form}
    template = 'customers/create.html'
    return render(request, template, context)