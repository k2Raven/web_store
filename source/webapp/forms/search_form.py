from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label="Найти")