from re import template
from django.views.generic import ListView
from .models import Customer

class CustomerListView(ListView):
    template_name = "customer/customer-list.html"
    model = Customer
    queryset = Customer.objects.all()