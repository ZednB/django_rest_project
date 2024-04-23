from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializers.payment import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('payed_course', 'payed_lesson', 'method')
    ordering_fields = ('payment_date',)
