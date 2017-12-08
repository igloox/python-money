from copy import deepcopy
from decimal import Decimal

from django import forms


class CurrencySelectWidget(forms.MultiWidget):
    """
    Custom widget for entering a value and choosing a currency
    """
    def __init__(self, choices=None, attrs={}):

        moneyInputAttrs = deepcopy(attrs)
        if 'size' not in moneyInputAttrs:
            moneyInputAttrs.update({'size': 5})

        widgets = (
            MoneyInput(attrs=moneyInputAttrs),
            forms.Select(attrs=attrs, choices=choices),
        )
        super(CurrencySelectWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        try:
            return [value.amount, value.currency]
        except:
            return [None, None]


class MoneyInput(forms.TextInput):
    # Overcome a limitation of the MutliValueField system whereby to set
    # a default currency we have to supply a whole Money object as
    # initial, which has the undesirable side-effect of also setting the
    # 'amount' field to '0', which looks wrong.
    def render(self, name, value, *args, **kwargs):
        if value == 0:
            value = ''
        return super(MoneyInput, self).render(name, value, *args, **kwargs)