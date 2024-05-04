from rest_framework import generics

from materials.paginators import LessonCoursePaginator
from materials.serializers.lesson import LessonSerializer
from materials.models import Lesson
from users.permissions import IsModerStaff, IsOwnerStaff
from rest_framework.permissions import IsAuthenticated, AllowAny


class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]
    pagination_class = LessonCoursePaginator


class LessonCreateApiView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny, IsOwnerStaff & ~IsModerStaff]

    def perform_create(self, serializer):
        user = serializer.save(owner=self.request.user)
        user.save()


class LessonRetrieveApiView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff | IsModerStaff]


class LessonUpdateApiView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff | IsModerStaff]


class LessonDestroyApiView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny, ~IsModerStaff | IsOwnerStaff]
