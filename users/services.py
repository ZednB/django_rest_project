import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def stripe_create_price(amount, product):
    price = stripe.Price.create(
        currency='RUB',
        amount=amount * 100,
        product=product,
    )
    return price.id

def create_session(price):
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/success",
        line_items=[{'price': price.get('id'), 'quantity': 1}],
        mode='payment',
    )
    return session.get('id'), session.get('url')
