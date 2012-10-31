from django import forms
from form_extensions.fields import USCurrencyField


class USCurrencyForm(forms.Form):
    price = USCurrencyField()