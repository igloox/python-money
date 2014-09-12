from django.conf import settings

CURRENCY_LABEL = getattr(settings, 'MONEY_CURRENCY_LABEL', u'%(code)s - %(name)s')
