from django import forms

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['picture', 'name', 'description',  'category', 'price']