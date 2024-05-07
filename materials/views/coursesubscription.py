from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, CourseSubscription
from materials.serializers.coursesubsription import CourseSubscriptionSerializer


class CourseSubscriptionCreateView(APIView):
    """Viewset for create"""
    def post(self, request):
        user = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = CourseSubscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            CourseSubscription.objects.create(
                user=user,
                course=course_item
            )
            message = 'Подписка добавлена'

        return Response({'message': message})

