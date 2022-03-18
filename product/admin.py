from django.contrib import admin
from .models import Product


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name", "description", "sale_price"]

