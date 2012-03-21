from copy import deepcopy

from django import forms
from money import Money, CURRENCY
from decimal import Decimal


class MoneyInput(forms.TextInput):
    # Overcome a limitation of the MutliValueField system whereby to set
    # a default currency we have to supply a whole Money object as
    # initial, which has the undesirable side-effect of also setting the
    # 'amount' field to '0', which looks wrong.
    def render(self, name, value, *args, **kwargs):
        if value == 0:
            value = ''
        return super(MoneyInput, self).render(name, value, *args, **kwargs)


class CurrencySelectWidget(forms.MultiWidget):
    """
    Custom widget for entering a value and choosing a currency
    """
    def __init__(self, choices=None, attrs={}):
        moneyInputAttrs = deepcopy(attrs)
        if not moneyInputAttrs.has_key('size'):
            moneyInputAttrs.update({'size': 5})

        widgets = (
            MoneyInput(attrs=moneyInputAttrs),
            forms.Select(attrs=attrs, choices=choices),
        )
        super(CurrencySelectWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        #print "CurrencySelectWidget decompress %s" % value
        if value:
            return [value.amount, value.currency]
        return [None,None]
