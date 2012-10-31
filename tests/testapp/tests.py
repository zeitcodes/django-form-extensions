"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .forms import HoneypotForm, HoneypotInitForm, USCurrencyForm, CreditCardForm
from .forms import HTMLForm, HTMLTagsForm, HTMLAttrsForm, HTMLStylesForm, HTMLEleReplaceForm

class HoneypotFieldTests(TestCase):

    def test_correct(self):
        data = {
            'target': ''
        }
        form = HoneypotForm(data)
        self.assertTrue(form.is_valid())

    def test_correct2(self):
        data = {
            'target': 'something'
        }
        form = HoneypotInitForm(data)
        self.assertTrue(form.is_valid())

    def test_incorrect(self):
        data = {
            'target': 'bot'
        }
        form = HoneypotForm(data)
        self.assertFalse(form.is_valid())

    def test_incorrect2(self):
        data = {
            'target': 'anything'
        }
        form = HoneypotInitForm(data)
        self.assertFalse(form.is_valid())

class HTMLFieldTests(TestCase):

    def test_not_escaped(self):
        data = {
            'html': '<p>This is an example</p>'
        }
        form = HTMLForm(data)
        self.assertTrue(form.is_valid())

    def test_escaped(self):
        data = {
            'html': '<p>This is <b>another</b> example</p>'
        }
        form = HTMLForm(data)
        self.assertTrue(form.is_valid())


class USCurrencyFieldTests(TestCase):

    def test_correct(self):
        data = {
            'price': '12'
        }
        form = USCurrencyForm(data)
        self.assertTrue(form.is_valid())

    def test_incorrect(self):
        data = {
            'price': 'cat',
        }
        form = USCurrencyForm(data)
        self.assertFalse(form.is_valid())

    def test_invalid_chars(self):
        data = {
            'price': '@234#45.3#'
        }
        form = USCurrencyForm(data)
        self.assertFalse(form.is_valid())

    def test_with_commas(self):
        data = {
            'price': '1,000'
        }
        form = USCurrencyForm(data)
        self.assertTrue(form.is_valid())

    def test_with_dollar_sign(self):
        data = {
            'price': '$100'
        }
        form = USCurrencyForm(data)
        self.assertTrue(form.is_valid())

    def test_with_decimal(self):
        data = {
            'price': '123.00'
        }
        form = USCurrencyForm(data)
        self.assertTrue(form.is_valid())

class CreditCardFieldTests(TestCase):

    def test_correct(self):
        data = {
            'number': '4000001234567899'
        }
        form = CreditCardForm(data)
        self.assertTrue(form.is_valid())

    def test_incorrect(self):
        data = {
            'number': '1234567890123456'
        }
        form = CreditCardForm(data)
        self.assertFalse(form.is_valid())