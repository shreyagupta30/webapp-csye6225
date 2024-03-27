from django.urls import include, path
from .views import UserAuthViewSet, GetUserAuthViewSet, UserEmailVerificationViewSet

urlpatterns = [
    path('v1/user', UserAuthViewSet.as_view(), name='user_auth'),
    path('v1/user/self', GetUserAuthViewSet.as_view(), name='user_self'),
    path('v1/user/verify', UserEmailVerificationViewSet.as_view(), name='user_verify'),
]
