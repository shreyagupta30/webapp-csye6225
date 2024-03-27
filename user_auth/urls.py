from django.urls import include, path
from .views import UserAuthViewSet, GetUserAuthViewSet, UserAuthVerificationViewSet

urlpatterns = [
    path('v1/user', UserAuthViewSet.as_view(), name='user_auth'),
    path('v1/user/self', GetUserAuthViewSet.as_view(), name='user_self'),
    path('v1/user/verify', UserAuthVerificationViewSet.as_view(), name='user_verify'),
]
