from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from materials.paginators import LessonCoursePaginator
from materials.serializers.course import CourseSerializer
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
