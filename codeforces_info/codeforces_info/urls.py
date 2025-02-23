# codeforces_info/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),  # Include userprofile URLs
]
