from django import forms

from .models import Order


class OrderDoneForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['status']