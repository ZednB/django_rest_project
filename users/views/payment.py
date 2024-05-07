from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializers.payment import PaymentSerializer
from rest_framework import generics

from materials.services import stripe_create_course
from users.services import stripe_create_price


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payed_course', 'payed_lesson', 'method')
    ordering_fields = ('payment_date',)


class PaymentListApiView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentCreateApiView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        if payment.payed_course:
            product = payment.payed_course.product_id
        else:
            product = payment.payed_lesson.product_id
        price = stripe_create_price(payment.amount, product, payment.currency)
        session, payment_url = stripe_create_course(price, description=payment.description)
        payment.payment_session = session
        payment.payment_url = payment_url
        payment.save()
