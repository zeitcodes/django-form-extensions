from django import forms
from form_extensions.fields import HoneypotField, HTMLField, USCurrencyField, CreditCardField


ALLOWED_TAGS = ['a', 'em', 'h1', 'h2', 'p', 'strong']
ALLOWED_ATTRIBUTES = ['class','id','style','title',]
ALLOWED_STYLES = {
    '*': ['display', 'clear', 'text-align'],
    'p': ['border*'],
}
ELEMENT_REPLACEMENTS = {
    'b': 'strong',
    'i': 'em',
    's': 'del',
    'strike': 'del',
    'u': 'ins',
}


class HoneypotForm(forms.Form):
    target = HoneypotField()

class HoneypotInitForm(forms.Form):
    target = HoneypotField(initial='something')

class HTMLForm(forms.Form):
    html = HTMLField(ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES, ELEMENT_REPLACEMENTS)

class HTMLTagsForm(forms.Form):
    html = HTMLField(ALLOWED_TAGS)

class HTMLAttrsForm(forms.Form):
    html = HTMLField(ALLOWED_TAGS, ALLOWED_ATTRIBUTES)

class HTMLStylesForm(forms.Form):
    html = HTMLField(ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES)

class HTMLEleReplaceForm(forms.Form):
    html = HTMLField(ALLOWED_TAGS, element_replacements=ELEMENT_REPLACEMENTS)

class USCurrencyForm(forms.Form):
    price = USCurrencyField()

class CreditCardForm(forms.Form):
    number = CreditCardField()