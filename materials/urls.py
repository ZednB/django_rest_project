from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.views.course import *
from materials.views.coursesubscription import CourseSubscriptionCreateView
from materials.views.lesson import *

from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    # lessons
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreateApiView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', LessonRetrieveApiView.as_view(), name='lesson_retrieve'),
    path('lesson/update/<int:pk>/', LessonUpdateApiView.as_view(), name='lesson_update'),
    path('lesson/destroy/<int:pk>/', LessonDestroyApiView.as_view(), name='lesson_destroy'),

    # subscribtion
    path('subscription/', CourseSubscriptionCreateView.as_view(), name='subscription')
] + router.urls
