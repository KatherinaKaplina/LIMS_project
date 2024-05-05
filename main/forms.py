from django import forms

class QuantityForm(forms.Form):
    quantity = forms.DecimalField(min_value=0.01, decimal_places=2)