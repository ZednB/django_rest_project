from rest_framework import generics
from materials.serializers.lesson import LessonSerializer
from materials.models import Lesson
from users.permissions import IsModerStaff, IsOwnerStaff
from rest_framework.permissions import IsAuthenticated


class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonCreateApiView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerStaff & ~IsOwnerStaff]

    def perform_create(self, serializer):
        user = serializer.save(user=self.request.user)
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
    permission_classes = [IsAuthenticated, ~IsModerStaff | IsOwnerStaff]
