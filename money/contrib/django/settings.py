from django.conf import settings

CURRENCY_LABEL = getattr(settings, 'CURRENCY_LABEL', u"%(code)s - %(name)s")
