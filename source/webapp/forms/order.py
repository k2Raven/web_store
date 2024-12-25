from django import forms

from webapp.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'phone', 'address']