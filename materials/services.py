import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def stripe_create_course(name):
    course = stripe.Product.create(
        name=name
    )
    return course.get('id')


def stripe_create_lesson(name, description):
    lesson = stripe.Product.create(
        name=name,
        description=description
    )
    return lesson.get('id')
