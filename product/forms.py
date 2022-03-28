from django import forms
from .models import Product

class DateInput(forms.DateInput):
    input_type = "date"

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField()
    sale_price = forms.FloatField()
    purchase_price = forms.FloatField()
    quantity = forms.IntegerField()
    purchase_date = forms.DateField(widget=DateInput()) 

    class Meta:
        model = Product
        fields = [
            'product_name',
            'description',
            'sale_price',
            'purchase_price',
            'quantity',
            'purchase_date',
        ]