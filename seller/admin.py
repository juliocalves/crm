from django.contrib import admin
from .models import Seller


@admin.register(Seller)

class SellerAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "email", "phone_number"]

