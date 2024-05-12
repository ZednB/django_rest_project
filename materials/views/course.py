from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, CourseSubscription
from materials.paginators import LessonCoursePaginator
from materials.serializers.course import CourseSerializer
from materials.tasks import send_course_update
from users.permissions import IsModerStaff, IsOwnerStaff
import stripe

stripe.api_key = settings.STRIPE_API_KEY


class CourseViewSet(ModelViewSet):
    """Viewset for course"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LessonCoursePaginator

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = (~IsModerStaff,)
        elif self.action == ['update']:
            self.permission_classes = (IsModerStaff | IsOwnerStaff)
        elif self.action == ['retrieve']:
            self.permission_classes = (IsModerStaff | IsOwnerStaff)
        elif self.action == ['destroy']:
            self.permission_classes = (~IsModerStaff | IsOwnerStaff)
        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save(user=self.request.user)
        user.save()

    def update(self, request, pk):
        course = self.get_object()
        serializer = self.get_serializer(course, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        subscribers = CourseSubscription.objects.filter(course=course.pk)
        email = [subscriber.user.email for subscriber in subscribers]
        send_course_update.delay(
            course_id=course.id,
            subject=f"Курс {course.name} был обновлен",
            message="Быстрее посмотрите что там нового",
            recipient_list=email
        )
        return Response(serializer.data)
