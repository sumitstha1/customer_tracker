from venv import create
from django.shortcuts import render, redirect

from app_customer.forms import CustomerCreateForm
from .models import Customer

# Create your views here.
def customer_index(request):
    template = 'customers/index.html'
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, template, context)

def customer_create(request):
    create_form = CustomerCreateForm()
    context = {"form": create_form}
    if request.method == "POST":
        # creating model object
        customer = Customer()

        # assigning value to attributes
        customer.first_name = request.POST.get('first_name')
        customer.middle_name = request.POST.get('middle_name')
        customer.last_name = request.POST.get('last_name')
        customer.email = request.POST.get('email')
        customer.password = request.POST.get('password')
        
        # storing value to db
        customer.save()

        context.setdefault("msg", "Successfully Added")
        template = 'customers/create.html'
        return render(request, template, context)

    template = 'customers/create.html'
    return render(request, template, context)

def customer_create(request):
    if request.method == 'POST':
        customer = Customer.objects.get(id=request.POST.get('id'))

        customer.first_name = request.POST.get('first_name')
        customer.middle_name = request.POST.get('middle_name')
        customer.last_name = request.POST.get('last_name')
        customer.email = request.POST.get('email')
        customer.password = request.POST.get('password')

        customer.save()

        return redirect('customer.index')
    return redirect('customer.index')

def customer_edit(request, id):
    customer = Customer.objects.get(id=id)
    template = 'customer/edit.html'
    context = {'customer': customer}
    return render(request, template, context)
    

