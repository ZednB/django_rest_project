from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from materials.models import Course
from materials.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
