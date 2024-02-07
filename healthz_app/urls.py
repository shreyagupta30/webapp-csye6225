from django.urls import include, path
from .views import DBHealthCheck

urlpatterns = [
    path('healthz', DBHealthCheck.as_view(), name='healthz'),
]
