
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views.payment import PaymentViewSet
from users.views.users import UserViewSet

app_name = UsersConfig.name

course_router = DefaultRouter()
course_router.register(r'user', UserViewSet, basename='user')
course_router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [

              ] + course_router.urls
