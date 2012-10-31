"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .forms import USCurrencyForm


class USCurrencyFieldTests(TestCase):
    def test_1(self):
        data = {
            'price': 'cat',
        }
        form = USCurrencyForm(data)
        self.assertTrue(form.is_valid())