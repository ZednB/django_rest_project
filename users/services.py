import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def stripe_create_product(payed_course):
    return stripe.Product.create(
        name=payed_course
    )


def stripe_create_price(amount, product):
    return stripe.Price.create(
        currency='rub',
        unit_amount=int(amount) * 100,
        product=product.get('id'),
    )


def create_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/success",
        line_items=[{'price': price.get('id'), 'quantity': 1}],
        mode='payment',
    )
    return session.get('id'), session.get('url')
