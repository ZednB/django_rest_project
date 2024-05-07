import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def stripe_create_price(amount, product_id):
    price = stripe.Price.create(
        currency='rub',
        unit_amount=amount * 100,
        product=product_id,
    )
    return price.get('id')


def create_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/success",
        line_items=[{'price': price.get('id'), 'quantity': 1}],
        mode='payment',
    )
    return session.get('id'), session.get('url')
