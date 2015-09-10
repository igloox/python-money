from django.utils.translation import ugettext_lazy as _
from django import forms
from widgets import CurrencySelectWidget
from money import Money, CURRENCY
from money.contrib.django.settings import CURRENCY_LABEL


class MoneyField(forms.MultiValueField):
    """
    A MultiValueField to represent both the quantity of money and the currency
    """

    def label_from_currency(self, c):
        return CURRENCY_LABEL % {'code': c.code, 'name': c.name,
                                 'symbol': c.symbol}

    def __init__(self, choices=None, decimal_places=2, max_digits=12,
                 default_currency=None, min_value=None, max_value=None,
                 *args, **kwargs):
        # Note that we catch args and kwargs that must only go to one field
        # or the other. The rest of them pass onto the decimal field.
        choices = choices or list(( (u"%s" % (c.code,), self.label_from_currency(c)) for i, c in sorted(CURRENCY.items()) if c.code != 'XXX'))

        self.widget = CurrencySelectWidget(choices)

        fields = (
            forms.DecimalField(*args, decimal_places=decimal_places,
                               min_value=min_value, max_value=max_value,
                               max_digits=max_digits, **kwargs),
            forms.ChoiceField(choices=choices)
        )

        if default_currency:
            kwargs.update({'initial': Money('', default_currency)})

        super(MoneyField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        """
        Take the two values from the request and return a single data value
        """
        if data_list:
            return Money(*data_list)
        return None
