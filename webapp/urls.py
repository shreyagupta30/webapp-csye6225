from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework import permissions

urlpatterns = [
    # Admin Routes
    path('admin/', admin.site.urls),

    # Application Routes
    path('', include('healthz_app.urls')),
    path('', include('user_auth.urls')),
]
