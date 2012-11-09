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

    def test_tags_no_change(self):
        input = '<p>Testing tags.</p>'
        data = {
            'html': input
        }
        form = HTMLTagsForm(data)
        self.assertTrue(form.is_valid())
        output = form.cleaned_data['html']
        self.assertEqual(input, output)

    def test_tags_removes_tags(self):
        input = '<d>This should be without tags after.</d>'
        data = {
            'html': input
        }
        form = HTMLTagsForm(data)
        self.assertTrue(form.is_valid())
        output = form.cleaned_data['html']
        self.assertEqual(input, output)

    def test_tags_escaped(self):
        data = {
            'html': '<p>This has an <b>escaped</b> tag.</p>'
        }
        form = HTMLTagsForm(data)
        self.assertTrue(form.is_valid())
        expected = '<p>This has an &lt;b&gt;escaped&lt;/b&gt;tag.</p>'
        output = form.cleaned_data['html']
        self.assertEqual(expected, output)

    def test_attrs_no_change(self):
        input = '<p class="example">Testing attributes.</p>'
        data = {
            'html': input
        }
        form = HTMLAttrsForm(data)
        self.assertTrue(form.is_valid())
        output = form.cleaned_data['html']
        self.assertEqual(input, output)

    def test_attrs_remove(self):
        data = {
            'html': '<p align="right">Testing attributes.</p>'
        }
        form = HTMLTagsForm(data)
        self.assertTrue(form.is_valid())
        expected = '<p>Testing attributes.</p>'
        output = form.cleaned_data['html']
        self.assertEqual(expected, output)

    def test_styles_no_change(self):
        input = '<p style="border: 2px solid black;">Testing styles.</p>'
        data = {
            'html': input
        }
        form = HTMLStylesForm(data)
        self.assertTrue(form.is_valid())
        output = form.cleaned_data['html']
        self.assertEqual(input, output)

    def test_styles_remove(self):
        data = {
            'html': '<p style="background-color:red;">Testing styles.</p>'
        }
        form = HTMLTagsForm(data)
        self.assertTrue(form.is_valid())
        expected = '<p>Testing styles.</p>'
        output = form.cleaned_data['html']
        self.assertEqual(expected, output)

    def test_element_replace_no_change(self):
        data = {
            'html': '<b>Testing element replacements.</b>'
        }
        form = HTMLEleReplaceForm(data)
        self.assertTrue(form.is_valid())
        expected = '<strong>Testing element replacements.</strong>'
        output = form.cleaned_data['html']
        self.assertEqual(expected, output)

    def test_element_replace_escaped(self):
        data = {
            'html': '<p>Testing element <t>replacements</t>.</p>'
        }
        form = HTMLTagsForm(data)
        self.assertTrue(form.is_valid())
        expected = '<p>Testing element &lt;t&gt;replacements&lt;/t&gt;.</p>'
        output = form.cleaned_data['html']
        self.assertEqual(expected, output)


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
