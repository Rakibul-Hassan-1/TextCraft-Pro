from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userinfo/', include('userinfo.urls')),  # Include the 'userinfo' app URLs
]
