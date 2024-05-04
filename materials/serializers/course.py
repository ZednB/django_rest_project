from rest_framework import serializers

from materials.models import Course, Lesson, CourseSubscription


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson_view = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    def get_lesson_view(self, instance):
        lesson_view = Lesson.objects.filter(course=instance).values()
        return lesson_view

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=obj).exists()
        return False
