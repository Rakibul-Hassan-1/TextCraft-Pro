from django.contrib import admin
from django.urls import path, include
from .views import landing_page  # Import landing page view
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),  # Set the landing page as the root URL
    path('accounts/', include('accounts.urls')),
    path('canvas/', include('canvas.urls')),
    path('chat/', include('chat.urls')),
    path('projects/', include('projects.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', accounts_views.register, name='register'),
    path('', include('accounts.urls')),  # Ensure correct app inclusion
]
