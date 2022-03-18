from django.urls import path
from .views import SellerListView

app_name = "seller"
urlpatterns = [
    path('list/',SellerListView.as_view(), name = 'seller-list')
]