from django import forms

from webapp.models import Cart


class CartFrom(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('qty',)
