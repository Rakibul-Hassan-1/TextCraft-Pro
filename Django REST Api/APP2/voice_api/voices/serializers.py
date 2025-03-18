from rest_framework import serializers
from .models import VoiceModel

class VoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceModel
        fields = '__all__'
