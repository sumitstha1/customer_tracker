from django.db import models

# Create your models here.
class UserApp(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    contact_number = models.IntegerField(max_length=20)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'pt_user'


class Customer(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_middle_name = models.CharField(max_length=100, null=True, blank=True)
    customer_last_name = models.CharField(max_length=100)
    customer_contact_number = models.IntegerField(max_length=20)
    customer_email = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=200)

    class Meta:
        db_table = 'pt_customer'