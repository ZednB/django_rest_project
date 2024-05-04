from rest_framework import serializers

from materials.models import CourseSubscription


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'