from django.db import models

class VoiceModel(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50, choices=[('bn', 'Bengali'), ('en', 'English')])
    voice_file = models.FileField(upload_to="voices/", blank=True, null=True)  # Store generated audio

    def __str__(self):
        return f"{self.name} ({self.language})"

from django.db import models

