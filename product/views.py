from re import template
from django.views.generic import ListView,CreateView
from .models import Product
from .forms import ProductForm
from django.urls import reverse

class ProductListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    queryset = Product.objects.all()

class ProductCreateView(CreateView):
    template_name ='product/product.html'
    form_class = ProductForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product:product-list')