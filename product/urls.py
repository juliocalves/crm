from django.urls import path
from .views import ProductListView, ProductCreateView

app_name = 'product'

urlpatterns = [
    path('list/', ProductListView.as_view(), name = 'product-list'),
    path('', ProductCreateView.as_view(), name = 'product-create')
]