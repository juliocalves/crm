from re import template
from django.views.generic import ListView, CreateView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse

class CustomerListView(ListView):
    template_name = "customer/customer-list.html"
    model = Customer
    queryset = Customer.objects.all().filter(active=True)

class CustomerCreateView(CreateView):
    template_name = 'customer/customer.html'
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:customer-list')