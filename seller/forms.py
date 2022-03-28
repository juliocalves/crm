from django import forms
from .models import Seller

class DateInput(forms.DateInput):
    input_type = "date"

class SellerForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'identification-first-name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'identification-last-name'}))
    birth_date = forms.DateField(widget=DateInput(attrs={'class':'identification-birth-date'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'class':'identification-cpf'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'contact-email'}))  
    area_code = forms.CharField(widget=forms.TextInput(attrs={'class':'contact-area-code'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'contact-phone-number'}))   

    cep = forms.CharField(widget=forms.TextInput(attrs={'class':'address-cep'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'address-country'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'address-state'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'address-city'}))
    street = forms.CharField(widget=forms.TextInput(attrs={'class':'address-street'}))
    street_number = forms.CharField(widget=forms.TextInput(attrs={'class':'address-street-number'}))

    class Meta:
        model = Seller
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "cpf",
            "email", 
            "area_code",
            "phone_number",
            "cep",
            "country",
            "state",
            "city",
            "street",
            "street_number",
        ]