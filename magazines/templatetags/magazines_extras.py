import uuid
from django import template
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

register = template.Library()


def paypal_form_for(magazine, user):

    if user.is_subscribed(magazine):
        html = "Subscribed!"
    else:
        papal_dict = {
            "business": settings.PAYPAL_RECIEVER_EMAIL,
            "currency_code": "EUR",
            "cmd": "_xclick-subscriptions",
            "a3": magazine.price,
            "p3": 1,
            "t3": "M",
            "src": 1,
            "sra": 1,
            "item_name": magazine.name,
            "invoice": uuid.uuid4(),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL,
            "custom": "%s-%s" % (magazine.pk, user.id)
        }

        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=papal_dict, button_type='subscribe').sandbox()
        else:
            html = PayPalPaymentsForm(initial=papal_dict, button_type='subscribe').render()

    return html

register.simple_tag(paypal_form_for)
