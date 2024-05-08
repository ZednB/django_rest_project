from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializers.payment import PaymentSerializer
from rest_framework import generics

from materials.services import stripe_create_course
from users.services import stripe_create_price, create_session, stripe_create_product


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payed_course', 'payed_lesson', 'method')
    ordering_fields = ('payment_date',)


class PaymentListApiView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_course', 'payed_lesson', 'method')
    ordering_fields = ('payment_date',)


class PaymentCreateApiView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user, method='cash')
        product = stripe_create_product(payment.payed_course)
        price = stripe_create_price(product=product, amount=payment.amount)
        session_id, session_url = create_session(price)
        payment.session_id = session_id
        payment.payment_link = session_url
        payment.save()

    # def perform_create(self, serializer):
    #     payment = serializer.save()
    #     user = self.request.user
    #     payment.user = user
    #     payment.save()
