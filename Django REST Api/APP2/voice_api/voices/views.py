from rest_framework import viewsets
from .models import VoiceModel
from .serializers import VoiceModelSerializer

class VoiceModelViewSet(viewsets.ModelViewSet):
    queryset = VoiceModel.objects.all()
    serializer_class = VoiceModelSerializer


import os
import logging
from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view
from gtts import gTTS
from .models import VoiceModel

logger = logging.getLogger(__name__)

@api_view(['POST'])
def generate_speech(request):
    try:
        data = request.data  
        text = data.get("text", "")
        voice_id = data.get("voice_id", None)

        if not text:
            return JsonResponse({"error": "Text input is required"}, status=400)

        try:
            voice_model = VoiceModel.objects.get(id=voice_id)
        except VoiceModel.DoesNotExist:
            return JsonResponse({"error": "Voice model not found"}, status=404)

        # Ensure voice_code exists in model
        language_code = voice_model.voice_code or "en"  # Default to English if missing

        # Generate speech
        tts = gTTS(text, lang=language_code)
        filename = f"speech_{voice_model.id}.mp3"
        filepath = os.path.join(settings.MEDIA_ROOT, "voices", filename)  # Save inside media/voices/
        
        # Create directory if not exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        tts.save(filepath)

        # Save file to model
        voice_model.voice_file = f"voices/{filename}"
        voice_model.save()

        # Provide file download link
        file_url = f"{request.scheme}://{request.get_host()}/media/voices/{filename}"

        return JsonResponse({
            "message": "Speech generated successfully.",
            "download_url": file_url
        })

    except Exception as e:
        logger.error(f"Error in generate_speech: {str(e)}", exc_info=True)
        return JsonResponse({"error": str(e)}, status=500)
