from django import forms
from app.models import Customers, Address

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        exclude = ()

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ()