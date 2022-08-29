from django.contrib import admin
from .models import UserApp, Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'password')
    list_filter = ('first_name', 'email')
    search_fields = ('first_name', 'email')

admin.site.register(UserApp)
admin.site.register(Customer, CustomerAdmin)

# Customizing site label
admin.site.site_title = "Admin-Panel"
admin.site.site_header = "Customer Tracker"
admin.site.index_title = "Welcome to Customer Tracker Admin Panel"