from django import forms

from models import TestMoneyModelDefaults
from money.contrib.django.forms import MoneyField
from money.contrib.django.forms import MoneyField

from money import Money


class TestDefaultCurrencyModelForm(forms.ModelForm):
	class Meta:
		model = TestMoneyModelDefaults


class TestDefaultCurrencyForm(forms.Form):
	price = MoneyField(default_currency='GBP')
