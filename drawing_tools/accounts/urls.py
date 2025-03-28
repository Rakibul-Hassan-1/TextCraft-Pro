from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    # other URL patterns...
    path('register/', views.register_view, name='register'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home_view, name='home'),

]
