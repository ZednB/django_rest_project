from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views.payment import PaymentViewSet
from users.views.users import UserCreateApiView, UserListApiView, UserRetrieveApiView, UserUpdateApiView, \
    UserDestroyApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions

app_name = UsersConfig.name

course_router = DefaultRouter()
# course_router.register(r'user', UserViewSet, basename='user')
course_router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register_user'),
    path('user/', UserListApiView.as_view(), name='list_user'),
    path('profile/<int:pk>/', UserRetrieveApiView.as_view(), name='profile_user'),
    path('update/<int:pk>/', UserUpdateApiView.as_view(), name='update_user'),
    path('destroy/<int:pk>/', UserDestroyApiView.as_view(), name='destroy_user'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(permissions.AllowAny,)), name='login_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + course_router.urls
