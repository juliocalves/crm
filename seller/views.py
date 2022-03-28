from re import template
from django.views.generic import ListView, CreateView
from .models import Seller
from .forms import SellerForm
from django.urls import reverse

class SellerListView(ListView):
    template_name = 'seller/seller-list.html'
    model = Seller
    queryset = Seller.objects.all()

class SellerCreateView(CreateView):
    template_name ='seller/seller.html'
    form_class = SellerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('seller:seller-list')