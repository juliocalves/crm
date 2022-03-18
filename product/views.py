from re import template
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    queryset = Product.objects.all()