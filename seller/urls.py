from django.urls import path
from .views import SellerListView, SellerCreateView

app_name = "seller"
urlpatterns = [
    path('list/',SellerListView.as_view(), name = 'seller-list'),
    path('',SellerCreateView.as_view(), name = 'seller-create')
]