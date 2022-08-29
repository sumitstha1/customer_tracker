from venv import create
from django.shortcuts import render, redirect

from app_customer.forms import CustomerCreateForm, UserRegisterForm
from .models import Customer

import string
import random

from django.core.mail import send_mail

# Create your views here.
def generate_random_string(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def user_register(request):
    user_reg_form = UserRegisterForm()
    template = 'users/register.html'
    if request.method == 'POST':
        user = UserRegisterForm(request.POST)
        if user.is_valid():
            user.save()

            chars = string.ascii_letters + string.punctuation
            size = 6
            verification_code = generate_random_string(size, chars)

            send_mail(
                'Email Verification',
                'Your verification code is: ' + verification_code,
                'edchristian.inventor@gmail.com',
                [request.POST.get('email')]
            )
        return render(request, template)
    context = {'form': user_reg_form}
    return render(request, template, context)


def customer_index(request):
    template = 'customers/index.html'
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, template, context)

def customer_show(request, id):
    template = 'customers/show.html'
    customer = Customer.objects.get(id=id)
    context = {'customer': customer}
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

def customer_update(request):
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
    template = 'customers/edit.html'
    context = {'customer': customer}
    return render(request, template, context)

def customer_delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()

    return redirect('customer.index')

    

