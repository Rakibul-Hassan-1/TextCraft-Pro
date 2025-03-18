from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Add fields you want to include in the form
