from re import template
from django.views.generic import ListView
from .models import Seller

class SellerListView(ListView):
    template_name = 'seller/seller-list.html'
    model = Seller
    queryset = Seller.objects.all()

